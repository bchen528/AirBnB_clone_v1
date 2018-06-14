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
        else:
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
        if line == "":
            for key, value in (storage.all()).items():
                a_list.append(value)
            print(a_list)
        elif line in self.classes:
            for key, value in (storage.all()).items():
                if key == "{}.{}".format(line, value.id):
                    #print(value.id)
                    a_list.append(value)
                    #print(key)
            print(a_list)
        else:
            print("** class doesn't exist **")

    def default(self, line):
        """method called on input line when command prefix is not recognized"""
        #print(line)
        #print(HBNBCommand.__dict__)
        args = shlex.split(line)
        #print(args)
        args = (line.strip('()')).split('.')
        #print(args)
        #print(" ".join(args))
        """for show and destroy"""
        plus_args = self.do_sdStrip(args[1])
        plus_args.append(args[0])
        #print(plus_args)
        #print(args)
        if len(plus_args) == 3:
            show_temp = plus_args[1]
            plus_args[1] = plus_args[2]
            plus_args[2] = show_temp
            sub_string = []
            sub_string.append(plus_args[1])
            sub_string.append(plus_args[2])
            #print(sub_string)
            #print(plus_args)
            args_string = " ".join(sub_string)
            #print(show_string)
            sd_fx_name = "do_" + plus_args[0]
            if sd_fx_name in HBNBCommand.__dict__:
                if sd_fx_name == "do_show":
                    self.do_show(args_string)
                if sd_fx_name == "do_destroy":
                    self.do_destroy(args_string)
            else:
                print("*** Unknown syntax: {}".
                      format(plus_args[1] + "." + plus_args[0] +
                             "({})".format(plus_args[2])))
        else:
            temp = args[0]
            args[0] = args[1]
            args[1] = temp
            #print(args)
            fx_name = "do_" + args[0]
            #print(fx_name)
            if fx_name in HBNBCommand.__dict__:
                line = " ".join(args)
                #print(HBNBCommand.__dict__[fx_name])
                if fx_name == "do_all":
                    self.do_all(args[1])
                elif fx_name == "do_count":
                    self.do_count(args[1])
                    #elif fx_name == "do_show":
                    #self.do_show(show_string)
                else:
                    print("*** Unknown syntax: {}".
                          format(args[1] + "." + args[0] + "()"))

    def do_count(self, line):
        """find number of instances of specific class"""
        num_instances = 0
        a_dict = storage.all()
        for key, value in a_dict.items():
            value = value.to_dict()
            if value['__class__'] == line:
                num_instances += 1
        print(num_instances)

    def do_sdStrip(self, line):
        """strip function arguments appropriately"""
        return (line.strip('"')).split('("')

    def do_destroy(self, argv):
        """deletes an instance based on the class name and id"""
        args = shlex.split(argv)

        if len(args) == 0 or args[0] == "":
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1 or args[1] == "":
            print("** instance id missing **")
        else:
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
        print()
        return True

if __name__ == '__main__':
    display = HBNBCommand()
    display.prompt = "(hbnb) "
    display.cmdloop()
