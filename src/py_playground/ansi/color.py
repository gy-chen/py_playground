class Color:
    """Store basic ANSI color.

        Stored color using (R, G, B) tuple.

        Use colors that used by xterm.

        See: https://en.wikipedia.org/wiki/ANSI_escape_code#3/4_bit
        """
    BLACK = (0, 0, 0)
    RED = (205, 0, 0)
    GREEN = (0, 205, 0)
    YELLOW = (205, 205, 0)
    BLUE = (0, 0, 238)
    MAGENTA = (205, 0, 205)
    CYAN = (0, 205, 205)
    WHITE = (229, 229, 229)


class ANSICode:
    RESET = 0


class ANSICodeBG:
    """Store basic ANSI color BG Code.

        See: https://en.wikipedia.org/wiki/ANSI_escape_code#3/4_bit
        """
    BLACK = 40
    RED = 41
    GREEN = 42
    YELLOW = 43
    BLUE = 44
    MAGENTA = 45
    CYAN = 46
    WHITE = 47


class ANSICodeFG:
    """Store basic ANSI color FG Code.

        See: https://en.wikipedia.org/wiki/ANSI_escape_code#3/4_bit
        """
    BLACK = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    MAGENTA = 35
    CYAN = 36
    WHITE = 37


MAP_COLOR_TO_ANSI_BG_CODE = {
    Color.BLACK: ANSICodeBG.BLACK,
    Color.RED: ANSICodeBG.RED,
    Color.GREEN: ANSICodeBG.GREEN,
    Color.YELLOW: ANSICodeBG.YELLOW,
    Color.BLUE: ANSICodeBG.BLUE,
    Color.MAGENTA: ANSICodeBG.MAGENTA,
    Color.CYAN: ANSICodeBG.CYAN,
    Color.WHITE: ANSICodeBG.WHITE
}

MAP_COLOR_TO_ANSI_FG_CODE = {
    Color.BLACK: ANSICodeFG.BLACK,
    Color.RED: ANSICodeFG.RED,
    Color.GREEN: ANSICodeFG.GREEN,
    Color.YELLOW: ANSICodeFG.YELLOW,
    Color.BLUE: ANSICodeFG.BLUE,
    Color.MAGENTA: ANSICodeFG.MAGENTA,
    Color.CYAN: ANSICodeFG.CYAN,
    Color.WHITE: ANSICodeFG.WHITE
}


def get_ansi_bg_code(color):
    return MAP_COLOR_TO_ANSI_BG_CODE[color]


def get_ansi_fg_code(color):
    return MAP_COLOR_TO_ANSI_FG_CODE[color]
