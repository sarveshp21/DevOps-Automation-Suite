# main entry point
from modules.cli import create_parser

def main():
    # create the command-line parser
    parser = create_parser()

    # read user input and parse command-line arguments
    args = parser.parse_args()

    # if no command is provided, display help
    if not hasattr(args, "func"):
        parser.print_help()
        return

    # execute the selected module
    args.func(args)

if __name__ == "__main__":
    main()
