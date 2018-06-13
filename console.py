#!/usr/bin/python3
"""This is a class HBNBCommand"""
import cmd
import json
import shlex
from sys import argv
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """class HBNBCommand"""
    classes = {"BaseModel", "User", "Place", "City", "State",
               "Amenity", "Review"}
    '''
    opts = {"create", "show", "all", "destroy", "update",
            "emptyline", "quit", "EOF", "help"}
    '''

    def do_create(self, cls):
        """create a new instance of BaseModel
        """
        if len(cls) == 0 or cls == "":
            print("** class name missing **")
        elif cls not in self.classes:
            print("** class doesn't exist **")
        else:
            new = eval(cls)()
            new.save()
            print(new.id)

    def do_show(self, argv):
        """prints string representation of an instance based on class name, id
        """
        args = shlex.split(argv)

        if len(args) == 0 or args[0] == "":
            print("** class name missing **")
        elif args[0] not in self.classes:
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
        a_list = []
        if line == "" or line in self.classes:
            for key, value in (storage.all()).items():
                a_list.append(value)
            print(a_list)
        else:
            print("** class doesn't exist **")

    '''
    def precmd(self, line):
        """executed before commandline line is interpreted,
            overrides built-in precmd
        Returns:
            commandline string to be interpreted
        """
        args = shlex.split(line)
        if len(args) == 1 and args[0] not in self.opts:
            args = (line.strip('()')).split('.')
            #print(args)
            temp = args[0]
            args[0] = args[1]
            args[1] = temp
            #print(args)
            #print(" ".join(args))
            return " ".join(args)
        return line
    '''

    def do_destroy(self, argv):
        """deletes an instance based on the class name and id"""
        args = shlex.split(argv)

        if len(args) == 0 or args[0] == "":
            print("** class name missing **")
        elif args[0] not in self.classes:
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

    def do_update(self, argv):
        """updates an instance based on the class name and id by
        adding or updating attribute
        """
        args = shlex.split(argv)

        if len(args) == 0 or args[0] == "":
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1 or args[1] == "":
            print("** instance id missing **")
        elif len(args) == 2:
            a_dict = storage.all()
            key = args[0] + "." + args[1]
            if key not in a_dict:
                print("** no instance found **")
            else:
                print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            a_dict = storage.all()
            key = args[0] + "." + args[1]
            if key in a_dict:
                setattr(a_dict[key], args[2], args[3])
                storage.save()

    def emptyline(self):
        """override built-in emptyline and remove previous command history"""
        pass

    def do_quit(self, args):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """Exit"""
        return True

if __name__ == '__main__':
    display = HBNBCommand()
    display.prompt = "(hbnb) "
    display.cmdloop()
