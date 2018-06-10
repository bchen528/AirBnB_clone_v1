#!/usr/bin/python3
"""This is a class HBNBCommand"""
import cmd
from sys import argv
from models.base_model import BaseModel
from models import storage
import json


class HBNBCommand(cmd.Cmd):
    """class HBNBCommand"""
    def do_create(self, cls):
        """create a new instance of BaseModel
        """
        if cls == "":
            print("** class name missing **")
        elif cls != "BaseModel":
            print("** class doesn't exist **")
        else:
            new = BaseModel()
            storage.save()
            print(new.id)

    def do_show(self, argv):
        """prints string representation of an instance based on class name, id
        """

        args = "".join(argv)
        args = [i.strip() for i in args.split(' ')]
        if len(args) == 2:
            cls_id = args[0] + "." + args[1]
        flag = 0

        """
        print(args)
        print("\n".join(args))
        if len(args) == 2:
            print(cls_id)
        """
        if len(args) == 0 or args[0] == "":
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) == 1 or args[1] == "":
            print("** instance id missing **")
        elif len(args) == 2:
            for key, value in (storage.all()).items():
                if key == cls_id:
                    print(value)
                    flag = 1
            if flag == 0:
                print("** no instance found **")

    """
    def do_all(self, line):
        if line != "BaseModel":
            print("** class doesn't exist **")
        else:
            print(line.__str__())
    """

    """
    def parseline(self, line):
        parse commandline
        return cmd.Cmd.parseline(self, line)
    """

    def emptyline(self):
        pass

    def do_quit(self, args):
        """Quit command to exit the program
        """
        raise SystemExit

    def do_EOF(self, line):
        """Exit"""
        return True

    """
    def parse(argv):
        args = []
        for i in range(len(argv)):
            if 
            args.append = argv[1]
        return args
    """

if __name__ == '__main__':
    display = HBNBCommand()
    display.prompt = "(hbnb) "
    display.cmdloop()
