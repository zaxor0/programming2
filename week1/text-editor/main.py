#!/usr/bin/python3
from editor import Editor

def main():

    editor = Editor()
    
    print("# Insert Strings Test")
    editor.insert("Hello")
    print(editor)   # outputs Hello
    editor.insert(" CSC7302")
    print(editor)   # outputs Hello CSC7302
    editor.insert("!")
    print(editor)   # outputs Hello CSC7302!

    print("\n# Delete N Character Tests")
    editor.delete_last(1)   
    print(editor)   # outputs Hello CSC7302
    
    print("\n# Insert Strings Test")
    editor.insert("!!!")
    print(editor)   # outputs Hello CSC7302!!!

    # backwards throught the stack
    print("\n# Undo Tests")

    editor.undo()
    print(editor)   # outputs Hello CSC7302

    editor.undo()
    print(editor)   # outputs Hello CSC7302!

    editor.undo()
    print(editor)   # outputs Hello CSC7302

    editor.undo()
    print(editor)   # outputs Hello 

    editor.undo()
    print(editor)   # outputs empty string

main()
