import cmd

class CLI(cmd.Cmd):
    intro = "CLI shellga xush kelibsiz! Type help yoki ? to batafsil ma'lumot olish."
    prompt = "(CLI) "

    def do_hello(self, arg):
        """Hello buyrug'i"""
        print("Salom!")

    def do_exit(self, arg):
        """CLI shellni tark etish"""
        print("Xayr, CLI shelldan chiqib ketdingiz!")
        return True

if __name__ == "__main__":
    CLI().cmdloop()
