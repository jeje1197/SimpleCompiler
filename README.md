# SimpleC

SimpleC is a compiler that targets the C language.
Created by Joseph Evans

To run the compiler, run the python file 'run.py' from the command line
with 2 arguments (Source_File_Path, Destination_File_Path)
        
        python run.py input.txt output.c

If the code compiles successfully, a file will be generated at the specified
path.

------------------------------------
--- Language Basics ---

SimpleC is made up of statements separated by newlines. It looks quite
similar to something you would see in assembly.

Here is an example of a print statement in SimpleC:

    print "Hello World!"

A statement consists of a function and its arguments:

print - A function that prints something to the console. It takes in one
argument.
    syntax:
        print [argument]

    ex.
        print "Hello World!"
        print 12 * 12

Data types in SimpleC:
    String, Int

    ex:
        "This is a string"
        123

Operators:
    +, -, *, /
