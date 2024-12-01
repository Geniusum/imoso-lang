class Lexical:
    Keywords = {
        "append": {"ltype": "keyword", "type": "append"},
        "set": {"ltype": "keyword", "type": "set"},
        "create": {"ltype": "keyword", "type": "create"},
        "save": {"ltype": "keyword", "type": "save"}
    }

    class Comments:
        ONE_LINE = {"ltype": "comment", "type": "oneline"}
        START = {"ltype": "comment", "type": "start"}
        END = {"ltype": "comment", "type": "end"}
    
    Operators = {
        "to": {"ltype": "operators", "type": "to"},
        "as": {"ltype": "operators", "type": "as"}
    }

class Other:
    class Char:
        LOWER_LETTERS = [*"abcdefghijklmnopqrstuvwxyz"]
        UPPER_LETTERS = [*"ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
        LETTERS = LOWER_LETTERS + UPPER_LETTERS
        NUMBERS = [*"0123456789"]
        COMMA = ","
        SEMICOLON = ";"
        POINT = "."
        DASH = "-"
        UNDERSCORE = "_"
        OPENING_BRACE = "{"
        CLOSING_BRACE = "}"
        OPENING_HOOK = "["
        CLOSING_HOOK = "]"
        OPENING_PARENTHESIS = "("
        CLOSING_PARENTHESIS = ")"
        AT = "@"
        WAVE = "~"
        SPACE = " "
        NEW_LINE = "\n"

        KW_NAME = LETTERS + [DASH]