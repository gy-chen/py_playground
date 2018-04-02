import os
from concurrent.futures import ThreadPoolExecutor
import logging
from .file import overwrite_with_t2c_content

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def overwrite_directory_files_with_t2s_content(directory, include_suffixies=None):
    executor = ThreadPoolExecutor()
    for root, _, files in os.walk(directory):
        for file_name in files:
            file = os.path.join(root, file_name)
            if include_suffixies is not None:
                for include_suffix in include_suffixies:
                    if file.endswith(include_suffix):
                        break
                else:
                    logger.debug('ignore file {} because of suffix setting.'.format(file))
                    continue
            executor.submit(overwrite_with_t2c_content, file)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    overwrite_directory_files_with_t2s_content('.', ['.html'])
