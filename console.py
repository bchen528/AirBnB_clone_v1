#!/usr/bin/python3
"""This is a class HBNBCommand"""
import cmd
from sys import argv
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """class HBNBCommand"""

    def do_create(self, cls):
        """create a new instance of BaseModel
        """
        print(cls)
        if cls == "":
            print("** class name missing **")
        elif cls != "BaseModel":
            print("** class doesn't exist **")
        else:
            new = BaseModel()
            storage.save()
            print(new.id)

    def do_show(self, line):
        """prints string representation of an instance based on class name, id
        """

        """
        if cls == "":
            print("** class name missing **")
        elif cls != "BaseModel":
            print("** class doesn't exist **")
        elif obj_id == "":
            print("** instance id missing **")
        elif type(obj_id).__name__ != "BaseModel":
            print("** no instance found **")
        else:
            print(obj_id.__str__())
        """
    """
    def do_all(self, cls):
        if cls != "BaseModel":
            print("** class doesn't exist **")
        else:
            print( __str__())
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

if __name__ == '__main__':
    display = HBNBCommand()
    display.prompt = "(hbnb) "
    display.cmdloop()
