import sys
import os
from .unicode import word_pattern


def find_unicode_words_recursively(path, suffixes=None):
    result = []
    for dir_path, _, names in os.walk(path):
        for name in names:
            if not _check_suffix(name, suffixes):
                continue
            try:
                with open(os.path.join(dir_path, name), encoding='utf8') as f:
                    content = f.read()
            except Exception as e:
                print(e, file=sys.stderr)
            else:
                result.extend(find_unicode_words(content))
    return result


def _check_suffix(name, valid_suffixes):
    if not valid_suffixes:
        return True
    return any(name.endswith(valid_suffix) for valid_suffix in valid_suffixes)


def find_unicode_words(content):
    """Find non-English words

        :param content:
        :return: list of words
        """
    return word_pattern.findall(content)


if __name__ == '__main__':
    for word in set(find_unicode_words_recursively('.', ['.js'])):
        print(word)
