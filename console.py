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

        if len(args) == 0 or args[0] == "":
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) == 1 or args[1] == "":
            print("** instance id missing **")
        elif len(args) == 2:
            a_dict = storage.all()
            key = args[0] + "." + args[1]
            if key in a_dict:
                print(a_dict[key])
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances based or not
        on the class name
        """
        if line != "BaseModel":
            print("** class doesn't exist **")
        else:
            for key, value in (storage.all()).items():
                print([value])

    def do_destroy(self, argv):
        """deletes an instance based on the class name and id"""
        args = "".join(argv)
        args = [i.strip() for i in args.split(' ')]

        if len(args) == 0 or args[0] == "":
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(args) == 1 or args[1] == "":
            print("** instance id missing **")
        elif len(args) == 2:
            a_dict = storage.all()
            key = args[0] + "." + args[1]
            if key in a_dict:
                del a_dict[key]
                storage.save()
            else:
                print("** no instance found **")

    def emptyline(self):
        pass

    def do_quit(self, args):
        """Quit command to exit the program
        """
        raise SystemExit

    def do_EOF(self, line):
        """Exit"""
        return True

if __name__ == '__main__':
    display = HBNBCommand()
    display.prompt = "(hbnb) "
    display.cmdloop()
