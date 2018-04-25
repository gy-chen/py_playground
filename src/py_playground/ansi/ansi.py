def generate_ansi_color_string(string, color):
    return "\033[{}m{}".format(color, string)


if __name__ == '__main__':
    from .color import Color, get_ansi_bg_code

    colors = (Color.RED,) * 3 + (Color.GREEN,) * 3 + (Color.BLUE,) * 3
    string = ''.join([generate_ansi_color_string(' ', get_ansi_bg_code(color)) for color in colors])
    print(string)
