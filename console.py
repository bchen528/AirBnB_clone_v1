#!/usr/bin/env python3
"""Command line module for python"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import json
from os import path
from models import storage
from shlex import split
from models.review import Review
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Simple command processor for python"""
    prompt = '(hbtn) '
    all_classes = ["BaseModel", "User", "State",
                   "City", "Amenity", "Place", "Review"]

    def do_create(self, line):
        """Creates a new BaseModel, saves it to storage
        Args:
            line (string): string of all the commands
        """
        if line:
            if line not in self.all_classes:
                print("** class doesn't exist **")
            else:
                new = eval(line)()
                storage.save()
                print(new.id)
        else:
            print("** class name missing **")

    def get_instance(self, line):
        """Returns an instance value
        Args:
            line (string): string of all the commands
        """
        if line:
            args = split(line)
            if args[0] not in self.all_classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                try:
                    base = args[0] + '.' + args[1]
                    for k, v in storage.all().items():
                        if k == base:
                            return v, args[1]
                    else:
                        print("** no instances found **")
                except Exception:
                    print("** no instance found **")
        else:
            print("** class name missing **")

    def get_attribute(self, line):
        """Gets the attribute name and value
        Args:
            line (string): string of all the commands
        """
        if line:
            args = split(line)
            if len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")

            if type(eval(args[3])) is int:
                return args[2], int(args[3])
            elif type(eval(args[3])) is float:
                return args[2], float(args[3])
            else:
                return args[2], args[3]

    def check_attr_value_type(self, attr, attr_value):
        """ """
        int_changes = ["number_rooms", "number_bathrooms",
                       "max_guest", "price_by_night"]
        float_changes = ["latitude", "longitude"]
        if attr in int_changes:
            return attr, int(attr_value)
        elif attr in float_changes:
            return attr, float(attr_value)
        else:
            return attr, attr_value

    def do_update(self, line):
        """Updates your base models
        Args:
            line (string): string of all the commands
        """
        try:
            model_value, model_id = self.get_instance(line)
            attr, attr_value = self.get_attribute(line)
            c_attr, c_attr_value = self.check_attr_value_type(attr, attr_value)
            setattr(model_value, c_attr, c_attr_value)
            storage.save()
        except Exception as e:
            print(e)

    def do_show(self, line):
        """Prints the string representations of an instance based
        on the class name and id
        ex: $show BaseModel 1234-1234-1234" # shows the entire dict
        Args:
            line (string): string of all the commands
        """
        try:
            model_value, model_id = self.get_instance(line)
            print("{}".format(model_value))
        except Exception:
            pass

    def do_all(self, line):
        """Prints all the string representations of all instances in file.json
        Args:
            line (string): string of all the commands
        """
        if line == "" or line in self.all_classes:
            try:
                obj_list = []
                n_dict = storage.all()
                for k, v in n_dict.items():
                    obj_list.append(v)
                print(obj_list)
            except Exception:
                print("** class doesn't exist **")

    def do_destroy(self, line):
        """Deletes an instance based on teh class name and id
        Args:
            line (string): string of all the commands
        """
        if line:
            args = split(line)
            if args[0] not in self.all_classes:
                print("** class doesn't exist **")
            elif len(args) != 2:
                print("** instance id missing **")
            else:
                flag = 1
                n_dict = storage.all()
                for k in n_dict.copy():
                    if args[1] == k.split('.')[1] and\
                       args[0] == k.split('.')[0]:
                        del n_dict[k]
                        flag = 0
                if flag:
                    print("** no instance found **")
                storage.save()
        else:
            print("** class name missing **")

    def do_quit(self, line):
        """Quit command to exit the program
        Args:
            line (string): string of all the commands
        """
        return True

    def emptyline(self):
        pass

    def do_EOF(self, line):
        """Exits the cmd
        Args:
            line (string): string of all the commands
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
