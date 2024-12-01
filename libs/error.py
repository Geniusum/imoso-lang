class Error():
    def __init__(self, type:str, reason:str, line:str, line_index:int, char_index:int) -> None:
        print(f"Error, {type.capitalize()}: {reason.capitalize()}.\nLn {line_index}, Col {char_index} :\n{line}\n{' ' * (char_index - 1)}^")