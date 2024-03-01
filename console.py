#!/usr/bin/python3
""" console.py """
import cmd


class HBNBCommand(cmd.Cmd):
    """ hbnb """
    prompt = '(hbnb) '
    
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()