#!/usr/bin/env python3
"""Command line module for python"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Simple command processor for python"""
    prompt = '(hbtn) '

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Exits the cmd"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
