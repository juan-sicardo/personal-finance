from cli.arguments import ArgumentParserManager


class CLIDriver:
    def __init__(self):
        pass

    @staticmethod
    def main():
        argument_parser_manager = ArgumentParserManager()
        arguments = argument_parser_manager.arguments


def main():
    clidriver = CLIDriver()
    clidriver.main()
