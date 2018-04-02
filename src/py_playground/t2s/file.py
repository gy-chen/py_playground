import io
import logging
from .dictionary import T2SDictionary

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

t2s_dictionary = T2SDictionary()


def overwrite_with_t2c_content(filepath):
    """Overwrite content of the file with traditional to simplified chinese translated content.

        :param filepath:
        :return:
        """
    with open(filepath, 'r', encoding='utf8') as f:
        content = f.read()
    translated = io.StringIO()
    for char in content:
        try:
            translated.write(t2s_dictionary.lookup(char))
            logger.debug("Translate {} to {}".format(char, t2s_dictionary.lookup(char)))
        except ValueError:
            translated.write(char)
            logger.debug("cannot find translation of character {}".format(char))
    with open(filepath, 'w', encoding='utf8') as f:
        f.write(translated.getvalue())
        logger.info("Write translated content to {}".format(filepath))
