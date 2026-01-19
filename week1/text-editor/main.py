#!/usr/bin/python3
from editor import Editor

def main():
    editor = Editor()
    
    editor.insert("Hello")
    print(editor)   # outputs Hello
    editor.insert(" CSC7302")
    print(editor)   # outputs Hello CSC7302
    editor.insert("!")
    print(editor)   # outputs Hello CSC7302!

    editor.delete_last(1)   
    print(editor)   # outputs Hello CSC7302
    
    editor.insert("!!!")
    print(editor)   # outputs Hello CSC7302!!!

    # backwards throught the stack
    print("undoing")

    editor.undo()
    print(editor)   # outputs Hello CSC7302

    editor.undo()
    print(editor)   # outputs Hello CSC7302!

    editor.undo()
    print(editor)   # outputs Hello CSC7302

    editor.undo()
    print(editor)   # outputs Hello 

main()
