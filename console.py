#!/usr/bin/python3
""" console.py """
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ hbnb """
    prompt = '(hbnb) '
    __my_class = ["BaseModel"]
    
    def do_quit(self, arg):
        """ Quit console """
        return True
    
    def do_EOF(self, arg):
        """ exit file with eof """
        print("")
        return True
    
    def emptyline(self):
        """ empty line """
        pass
    
    def do_create(self, arg):
        """ create class instance """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.__my_class:
            print("** class doesn't exist **")
        else:
            instance = eval(args[0])()
            storage.new(instance)
            print(instance.id)
            
    def do_show(self, arg):
        """ show str repr """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.__my_class:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = f"{args[0]}.{args[1]}"
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")
        
    def do_destroy(self, arg):
        """ Remove instance based id """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.__my_class:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = f"{args[0]}.{args[1]}"
            if key in objects:
                del objects[key]
                storage.save()
            else:
                print("** no instance found **")
    
    def do_all(self, arg):
        """ Print all string reprs """
        args = arg.split()
        if len(args) == 0 or args[0] in self.__my_class:
            objects = storage.all()
            for value in objects.values():
                print(str(value))
        else:
            print("** class doesn't exist **")
            
    def do_update(self, arg):
        """ update instance based id """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.__my_class:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")   
        else:
            objects = storage.all()
            key = f"{args[0]}.{args[1]}"
            if key in objects:
                obj = objects[key]
                setattr(obj, args[2], args[3])
                obj.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()