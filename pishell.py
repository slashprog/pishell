from command_dispatch import CommandDispatch

commands = CommandDispatch()

import os

@commands.action("mkdir")
def create_dir(cmd, *args): # mkdir
    for path in args:
        os.mkdir(path)
    
@commands.action("ls")
def listfiles(cmd, *args): # ls
    for path in args:
        print "%s:" % path
        for file in os.listdir(path):
            print "%s\t" % file, 
        print ""

@commands.action("pwd")
def show_dir(cmd, *args):  # pwd
    print os.getcwd()

@commands.action("date")
def show_time(cmd, *args):  # date
    from time import ctime
    print ctime()

@commands.action("exit")
def exit_program(cmd, *args): # exit
    print "Bye"
    exit(0)

def invalid_command(cmd, *args):
    print "Invalid command - ", cmd

def parse_command():
    cmd = raw_input("PiShell> ")
    args = cmd.split()
    cmd = args.pop(0)
    return cmd, args

commands.run(parse_command, invalid_command)

