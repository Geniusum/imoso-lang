from . import lexical
from . import utils
from . import error

class Parser():
    def __init__(self, content:str, end_func=utils.void, log:bool=False) -> None:
        self.content = content
        self.end_func = end_func
        self.log = log

    def parse(self):
        parsed = []

        lines = self.content.splitlines()

        actual_word = ""
        actual_raw = ""
        line_index = 1
        line_char_index = 0
        step = 0
        space_before = False
        last_char = False
        
        for char_index, char in enumerate(self.content):
            last_char = char_index + 1 == len(self.content)
            if char == lexical.Other.Char.NEW_LINE:
                line_index += 1
                line_char_index = 0
            else:
                line_char_index += 1
                if not (space_before and char == lexical.Other.Char.SPACE):
                    if char == lexical.Other.Char.SPACE:
                        space_before = True

                    if not step:
                        if char in lexical.Other.Char.KW_NAME:
                            actual_word += char.lower()
                        
                        if (char == lexical.Other.Char.SPACE or last_char):
                            step = 1
                            
                            parsed.append({
                                "type": "instruction",
                                "content": []
                            })

                            if not actual_word in lexical.Lexical.Keywords.keys():
                                error.Error("Syntax", "Not a valid keyword", lines[line_index - 1], line_index, line_char_index)
                                self.end_func()
                                break

                            parsed[-1]["content"].append(lexical.Lexical.Keywords[actual_word])

                            actual_word = ""
                            actual_raw = ""
                    elif step == 1:
                        if char in lexical.Other.Char.KW_NAME:
                            actual_word += char.lower()

                        if (char == lexical.Other.Char.SPACE or last_char):
                            if not actual_word in lexical.Lexical.Operators.keys():
                                # error.Error("Syntax", "Not a valid operator", lines[line_index - 1], line_index, line_char_index)
                                # self.end_func()
                                # break

                                parsed[-1]["content"].append
                            else:
                                parsed[-1]["content"].append(lexical.Lexical.Operators[actual_word])

                                actual_word = ""

                elif char != lexical.Other.Char.SPACE and space_before:
                    space_before = False