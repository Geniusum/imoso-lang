#!/usr/bin/python

#* Import

import sys, argparse, os, time
import libs.sourcecode as sourcecode
import libs.parser as parser

#* Main procedure

class Main():
    class FileNotFound(BaseException): ...
    class InvalidFileExtension(BaseException): ...

    def __init__(self, argv:list[str]) -> None:
        self.parser = argparse.ArgumentParser(prog="imoso interpreter", description="Interpretes .imo programs.")
        self.parser.add_argument("-l", "--log", action="store_true")
        self.parser.add_argument("-t", "--timer", action="store_true")
        self.parser.add_argument("filename", type=str)
        self.args = vars(self.parser.parse_args(argv))

        self.log:bool =     self.args["log"]
        self.timer:bool =   self.args["timer"]
        self.filename:str = self.args["filename"]

    def start(self):
        if self.timer:
            self.start_time = time.time()

        if not os.path.exists(self.filename):
            raise self.FileNotFound(self.filename)

        if os.path.splitext(os.path.basename(self.filename))[1].lower() != ".imo":
            raise self.InvalidFileExtension(os.path.basename(self.filename))

        sourcecode_content:str = open(self.filename, "r", encoding="utf-8").read().strip()

        self.sourcecode = sourcecode.SourceCode(sourcecode_content)
        self.parser = parser.Parser(self.sourcecode.content, end_func=self.end, log=self.log)
        self.parser.parse()

    def end(self):
        if self.timer:
            self.end_time = time.time()
            print(f"Program running time : {self.end_time - self.start_time}s")
        
        sys.exit()

if __name__ == "__main__":
    instance = Main(sys.argv[1:])
    instance.start()
    instance.end()