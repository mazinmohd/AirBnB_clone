#!/usr/bin/python3
"""entry point of the command interpreter"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """class HBNBCommand(cmd.Cmd):"""

    prompt = "(hbnb) "
    classes = ['BaseModel', 'User', 'Amenity',
               'Place', 'City', 'State', 'Review']

    def help_help(self):
        """help if u need help"""
        print("Help:\nhow to use\n\tcreate\tUsage: create <class name>\
              \n\n\tshow\tUsage: show <class name> <ID>\
              \n\n\tdestroy\tUsage: destroy <class name> <ID>\
              \n\n\tall\tUsage: all <class name > || all\
              \n\n\tupdate\tUsage: update <class name> <id> \
               <attribute name> <attribute value>")
        return
    ###################

    def do_EOF(self, line):
        """EOF"""
        return True

    def help_EOF(self):
        """help EOF"""
        print("EOF Quit the command interpreter\n")
    ########################

    def do_quit(self, line):
        """Quit"""
        return True

    def help_quit(self):
        """help Quit"""
        print("Quit the command interpreter\n")
    #############################

    def do_create(self, arg):
        """create obj"""
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            Models = {'BaseModel': BaseModel, 'User': User, 'Amenity': Amenity,
                      'Place': Place, 'City': City,
                      'State': State, 'Review': Review}
            my_model = Models[arg]()
            print(my_model.id)
            my_model.save()

    def help_create(self):
        """how to use create"""
        print("Usage: create <class name>")
        return

    def emptyline(self):
        """do nothing when empty line"""
        pass
    ###########################

    def do_show(self, line):
        """show obj info"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")

        elif len(args) < 2:
            print("** instance id missing **")
            return

        else:
            all_objs = storage.all()
            for key, value in all_objs.items():
                ob_name = value.__class__.__name__
                ob_id = value.id
                if ob_name == args[0] and ob_id == args[1]:
                    print(value)
                    return
            print("** no instance found **")

    def help_show(self):
        """help how to use show"""
        print("Usage: show <class name> <ID>")
        return

    #############################
    def do_destroy(self, line):
        """destroy obj at id"""
        args = line.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")

        elif len(args) < 2:
            print("** instance id missing **")
            return

        else:
            all_objs = storage.all()
            for key, value in all_objs.items():
                ob_name = value.__class__.__name__
                ob_id = value.id
                if ob_name == args[0] and ob_id == args[1]:
                    del value
                    del storage._FileStorage__objects[key]
                    storage.save()
                    return
            print("** no instance found **")

    def help_destroy(self):
        """help destroy"""
        print("Usage: destroy <class name> <ID>")
        return

    ##################

    def do_all(self, arg):
        """print all objs"""
        if arg and arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        all_objs = storage.all()
        instances = []
        for key, value in all_objs.items():
            ob_name = value.__class__.__name__
            if arg and ob_name == arg:
                instances += [value.__str__()]
            else:
                instances += [value.__str__()]
        print(instances)

    def help_all(self):
        """Help all"""
        print("all <class name > || all")
    ####################

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file). """
        args = line.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")

        elif len(args) < 2:
            print("** instance id missing **")
            return

        else:
            class_name = args[0]
            instance_id = args[1]

            objects = storage.all()
            key = f"{class_name}.{instance_id}"

            if key not in objects:
                print("** no instance found **")
                return

            if len(args) < 3:
                print("** attribute name missing **")
                return

            elif len(args) < 4:
                print("** value missing **")
                return

            value = args[3].replace('"', '')

            for key, objc in objects.items():
                ob_id = objc.id
                if ob_id == args[1]:
                    setattr(objc, args[2], value)
                    storage.save()
                    storage.reload()

    def help_update(self):
        """help Update"""
        print("Usage: update <class name> <id> \
              <attribute name> \"<attribute value>\"")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
