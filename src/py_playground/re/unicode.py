import re

# non English unicode word character
char_pattern = re.compile(r'[^\Wa-zA-Z0-9_]')

word_pattern = re.compile(r"(%s+)" % char_pattern.pattern)

if __name__ == '__main__':
    words = word_pattern.findall('盟興 dog 阿輝')
    print(words)
