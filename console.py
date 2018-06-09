#!/usr/bin/env python3
"""Command line module for python"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import json 
from os import path
from models import storage

class HBNBCommand(cmd.Cmd):
    """Simple command processor for python"""
    prompt = '(hbtn) '
    all_classes = ["BaseModel", "FileStorage"]    

    def do_create(self, line):
        """ """
        if line:
            if line not in self.all_classes:
                print("** class doesn't exist **")
            else:
                new = BaseModel()
                storage.save() 
                print(new.id)
        else:
            print("** class name missing **")

    def get_instance(self, line):
        """Returns an instance value"""
        if line:
            args = line.split()
            if args[0] not in self.all_classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                #search for id 
                try:
                    with open("file.json", mode='r', encoding='utf-8') as f:
                        flag = 1
                        for key, value in json.load(f).items():
                            if args[1] == key.split('.')[1]:
                                flag = 0
                                return args[0], args[1], value
                        if flag:
                            print("** no instance found **")
                except Exception:
                    print("** no instance found **")
        else:
            print("** class name missing **")
    
    def get_attribute(self, line):
        """Gets the attribute name and value"""
        if line:
            args = line.split()
            if len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            return args[2], args[3]
             
    def do_update(self, line):
        """ """
        try:
            model, model_id, model_value = self.get_instance(line)
            attr, attr_value = self.get_attribute(line)
        except Exception:
            pass

    def do_show(self, line):
        """Prints the string representations of an instance based 
        on the class name and id
        ex: $show BaseModel 1234-1234-1234" # shows the entire dict
        """
        try:
            model, model_id, model_value = self.get_instance(line)
            print("[{}] ({}) {}".format(model, model_id, model_value))
        except Exception:
            pass

    def do_all(self, line):
        """Prints all the string representations of all instances in file.json"""
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
        """Deletes an instance based on teh class name and id"""
        if line:
            args = line.split()
            if args[0] not in self.all_classes:
                print("** class doesn't exist **")
            elif len(args) != 2:
                print("** instance id missing **")
            else:
                flag = 1
                n_dict = storage.all()
                for k in n_dict.copy():
                    if args[1] == k.split('.')[1]:
                        del n_dict[k]
                        flag = 0
                if flag:
                    print("** no instance found **")
                storage.save() 
        else:
            print("** class name missing **")         

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Exits the cmd"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
