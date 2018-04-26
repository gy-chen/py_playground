from .color import get_ansi_bg_code


class ANSICode:
    RESET = 0


def generate_ansi_code_string(string, code):
    return "\033[{}m{}".format(code, string)


def generate_ansi_bg_color_string(string, color):
    return generate_ansi_code_string(string, get_ansi_bg_code(color))


ansi_reset_string = generate_ansi_code_string('', ANSICode.RESET)

if __name__ == '__main__':
    from .color import ANSIBasicColor, get_ansi_bg_code

    colors = (ANSIBasicColor.RED,) * 3 + (ANSIBasicColor.GREEN,) * 3 + (ANSIBasicColor.BLUE,) * 3
    string = ''.join([generate_ansi_code_string(' ', get_ansi_bg_code(color)) for color in colors])
    print(string)
