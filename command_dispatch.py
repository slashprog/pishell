class CommandDispatch:
    class Error(Exception): pass

    def __init__(self):
        self.commands = { }

    def action(self, c):
        def decorator(f):
            self.commands[c] = f
        return decorator

    def run(self, parser, invalid_command):
        while True:
            cmd, args = parser()
            self.commands.get(cmd, invalid_command)(cmd, *args)

            
