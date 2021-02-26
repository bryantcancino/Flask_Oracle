class Colors():
    dictionary = {
        "NULL": '\033[1;m',
        "GRAY": '\033[1;30m',
        "RED": '\033[1;31m',
        "GREEN": '\033[1;32m',
        "YELLOW": '\033[1;33m',
        "BLUE": '\033[1;34m',
        "MAGENTA": '\033[1;35m',
        "CYAN": '\033[1;36m',
        "WHITE": '\033[1;37m',
        "CRISMON": '\033[1;38m',
        "HIGHLIGHTED_RED": '\033[1;41m',
        "HIGHLIGHTED_GREEN": '\033[1;42m',
        "HIGHLIGHTED_BROWN": '\033[1;43m',
        "HIGHLIGHTED_BLUE": '\033[1;44m',
        "HIGHLIGHTED_MAGENTA": '\033[1;45m',
        "HIGHLIGHTED_CYAN": '\033[1;46m',
        "HIGHLIGHTED_GRAY": '\033[1;47m',
    }

    @staticmethod
    def print_color(color, message):
        print(Colors.dictionary.get(color)+message+Colors.dictionary.get("NULL"))

    @staticmethod
    def format(color, message):
        return Colors.dictionary.get(color)+message+Colors.dictionary.get("NULL")
