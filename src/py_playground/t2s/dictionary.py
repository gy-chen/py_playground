import os
import json
import urllib.request
import tempfile
import logging
import cerberus

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

t2s_dictionary_url = 'https://raw.githubusercontent.com/tongwentang/tongwen-core/master/dictionaries/t2s_char.json'

dictionary_schema = {
    'name': {
        'type': 'string'
    },
    'filename': {
        'type': 'string'
    },
    'type': {
        'type': 'string'
    },
    "enabled": {
        'type': 'boolean'
    },
    'map': {
        'type': 'dict',
        'keyschema': {
            'type': 'string',
            'regex': r'\S'
        },
        'valueschema': {
            'type': 'string',
            'regex': r'\S'
        }
    }
}


class T2SDictionary:
    """Provide function to translate character from traditional to simplified chinese.

        """

    def __init__(self, filepath=None):
        """

                :param filepath: the path of download
                """
        self._file = filepath or self._mkstemp()
        self._dictionary = None

        self._load_dictionary()

    def lookup(self, char):
        return lookup_dictionary(self._dictionary, char)

    def _mkstemp(self):
        return tempfile.TemporaryFile()

    def _load_dictionary(self):
        download_t2s_dictionary(self._file)
        if not isinstance(self._file, str):
            self._file.seek(0)
        self._dictionary = load_dictionary(self._file)


def download_t2s_dictionary(file, force=False):
    """Download t2s dictionary

        Skip download if filepath exists.

        :param file: file file object  or file path
        :param force: force download dictionary even file path exists
        :return:
        """
    close_file = False
    if isinstance(file, str):
        if os.path.exists(file) and not force:
            logger.info("t2s dictionary exists, ignore.")
            return
        file = open(file, 'wb')
        close_file = True
    logger.info("start to download dictionary")
    with urllib.request.urlopen(t2s_dictionary_url) as request:
        file.write(request.read())
    logger.info("t2s dictionary downloaded.")
    if close_file:
        file.close()


def load_dictionary(file):
    """Load dictionary file

        Expect file is JSON in following format:
        {
            "name": "dictionary name",
            "filename": "dictionary filename",
            "type": "dictioanry type",
            "enabled": boolean,
            "map": {
                "src char 1": "to char 1",
                "src char 2": "to char 2",
                ...
            }
        }

        :param file: file object or file path
        :return:
        """
    close_file = False
    if isinstance(file, str):
        file = open(file, 'r', encoding='utf8')
        close_file = True
    dictionary = json.load(file)
    if close_file:
        file.close()
    validator = cerberus.Validator(dictionary_schema)
    if not validator.validate(dictionary):
        raise ValueError(validator.errors)
    return dictionary


def lookup_dictionary(dictionary, char):
    """Lookup a word from dictionary

        :param dictionary:
        :param char:
        :return:
        """
    mapped = dictionary['map'].get(char)
    if mapped is None:
        raise ValueError("{} is not in the dictionary".format(char))
    return mapped


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    dictionary = T2SDictionary('t2s.json')
    print(dictionary.lookup('興'))
