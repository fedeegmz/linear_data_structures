from inspect import Attribute
from types import NoneType
from linked_lists.singly_linked_list import SinglyLinkedList

command_list = ['info','exit', 'new singly_linked_list', 'linked_list.append()', 
'linked_list.size()', 'linked_list.print()']

def start():
    print("Welcome to play_with_linked_list")


def loop():

    #variables needed
    linked_list = None

    finished = False
    while not finished:
        command = input()
        if command not in command_list:
            print("Please, enter a valid command")
            continue

        if command == 'info':
            pass
        
        elif command == 'new singly_linked_list':
            linked_list = SinglyLinkedList()
        
        elif command == 'linked_list.append()':
            try:
                data = input("Enter the data\n")
                linked_list.append(data)
            except AttributeError as ae:
                print("First, execute 'new singly_linked_list'")
                continue
        
        elif command == 'linked_list.size()':
            print(linked_list.size())

        elif command == 'linked_list.print()':
            for node in linked_list.iter():
                print(f'{node} in {id(node)}')
        
        elif command == 'exit':
            finished = True
            continue



if __name__ == '__main__':
    start()
    loop()