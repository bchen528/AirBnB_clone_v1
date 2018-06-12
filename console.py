#!/usr/bin/python3
"""This is a class HBNBCommand"""
import cmd
import json
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

    def do_create(self, cls):
        """create a new instance of BaseModel
        """
        if cls == "":
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
        args = "".join(argv)
        args = [i.strip() for i in args.split(' ')]

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

    def do_destroy(self, argv):
        """deletes an instance based on the class name and id"""
        args = "".join(argv)
        args = [i.strip() for i in args.split(' ')]

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
        args = "".join(argv)
        args = [i.strip() for i in args.split(' ')]

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
                subkey = args[2]
                """
                temp = [args[2], args[3]]
                subvalue = self.typecheck(temp)
                if type(subvalue) is str:
                """
                subvalue = args[3].replace('"', '')
                subdict = a_dict[key]
                setattr(subdict, subkey, subvalue)
                storage.save()

    '''
    def typecheck(self, arg):
        """typecast attributes appropriately
        Returns:
            typecasted argument
        """
        integers = ['number_rooms', 'number_bathrooms', 'max_guest',
                    'price_by_night']
        floats = ['latitude', 'longitude']
        if arg[0] in integers:
            arg[1] = int(arg[1])
        elif arg[0] in floats:
            arg[1] = float(arg[1])
        else:
            try:
                if type(eval(str(arg[1]))) is not str:
                    arg[1] = eval(str(arg[1]))
            except NameError:
                pass
        return arg[1]
    '''

    def emptyline(self):
        """override built-in emptyline and remove previous command history"""
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
