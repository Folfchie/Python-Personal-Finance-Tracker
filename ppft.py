import sys
import traceback
import modules as mods

# Command registry
commands = {}


def command(name):
    """Decorator to register commands."""
    def wrapper(func):
        commands[name] = func
        return func
    return wrapper


@command("hello")
def hello(args, opts):
    name = args[0] if args else "world"
    if "--shout" in opts:
        print(f"HELLO {name.upper()}!")
    else:
        print(f"Hello {name}.")


@command("help_me")
def help_me(args, opts):
    if '--extended' in opts:
        print("""
        
        PPFT commands:
        
        Command | Description | Usage | Options
        
        
        proc_mtd: Used for processing month-to-date workbooks. Usage: proc_mtd filename --options | verbose
        
        proc_ytd: Used for processing year-to-date workbooks. Usage: proc_ytd filename --options
        
        cwd: Used to view the current working directory. Usage: cwd
        
        cd: Used to change the current working directory. Usage: cd
        
        ls: List files and paths in current working directory. Usage: ls
        
        help: Displays a list of commands and usages. Usage: help --options | extended
        
                """)
    else:
        print("""
        
PPFT commands:
        
proc_income filename --options
proc_mtd filename --options
proc_ytd filename --options
cwd
cd
ls
quit
help --options
            """)


@command("proc_income")
def proc_income(args, opts):
    filename = args[0] if args else None
    if filename:
        try:
            mods.process_income_workbook(filename)
        except Exception as e:
            print('\nAn error occurred. Check the file name/path and try again.\n')
            if "--verbose" in opts:
                print("Error type:", type(e).__name__)
                print("Message:", str(e))
                traceback.print_exc()
                print("\n")
    else:
        print('\nNo file provided. Please provided a file name or path. \n')


def parse(argv):
    if not argv:
        print("No command given.")
        return

    cmd, *rest = argv
    args = [a for a in rest if not a.startswith("--")]
    opts = [o for o in rest if o.startswith("--")]

    if cmd in commands:
        commands[cmd](args, opts)
    else:
        print(f"Unknown command: {cmd}")


if __name__ == "__main__":
    parse(sys.argv[1:])
