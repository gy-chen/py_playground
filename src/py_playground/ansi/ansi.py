from .color import get_ansi_bg_code


class ANSICode:
    RESET = 0


def generate_ansi_code_string(string, code):
    return "\033[{}m{}".format(code, string)


def generate_ansi_bg_color_string(string, color):
    return generate_ansi_code_string(string, get_ansi_bg_code(color))


def get_ansi_reset_string():
    return generate_ansi_code_string('', ANSICode.RESET)


if __name__ == '__main__':
    from .color import Color, get_ansi_bg_code

    colors = (Color.RED,) * 3 + (Color.GREEN,) * 3 + (Color.BLUE,) * 3
    string = ''.join([generate_ansi_code_string(' ', get_ansi_bg_code(color)) for color in colors])
    print(string)
