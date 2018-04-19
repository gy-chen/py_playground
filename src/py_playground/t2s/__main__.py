from . import get_arg_parser
from .batch import overwrite_directory_files_with_t2s_content

parser = get_arg_parser()
args = parser.parse_args()

overwrite_directory_files_with_t2s_content(args.path, args.suffixes)
