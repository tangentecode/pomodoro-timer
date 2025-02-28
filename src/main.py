import time
import sys
import os
import pyfiglet
import random


def timer_custom(font: str, mins: int) -> None:
    """Runs a custom duration timer displaying time in the specified font.

    Args:
        font (str): The font to use for displaying the timer.
        mins (int): The duration of the timer in minutes.
    """
    clear_stdout()
    for i in range(mins - 1, -1, -1):
        for j in range(59, -1, -1):
            clear_stdout()
            print("\n" * (os.get_terminal_size().lines // 4))  # Center more vertically
            timer_text = pyfiglet.figlet_format(
                f"{i:02}:{j:02}", font=font
            )  # Format with leading zeros
            centered_text = "\n".join(
                line.center(os.get_terminal_size().columns)
                for line in timer_text.split("\n")
            )
            print(centered_text)  # Print FIGlet text
            time.sleep(1)


def options() -> bool:
    """Prompts the user for automatic break options.

    Returns:
        bool: True if the user wants automatic breaks, False otherwise.
    """
    while True:
        choice = input("Automatically select break after pomodoro? [Y]es/[N]o ").lower()
        if choice == "y":
            return True
        elif choice == "n":
            return False
        else:
            print("Invalid option, please enter 'Y' or 'N'.")


def clear_stdout() -> None:
    """Clears the console screen."""
    sys.stdout.write("\033[H\033[J")  # ANSI escape code to clear the screen
    sys.stdout.flush()


def main() -> None:
    """Handles user input and timer selection."""
    try:
        if sys.argv[1] == "--random":
            font: str = random.choice(pyfiglet.FigletFont.getFonts())
        elif sys.argv[1] in ("-f", "--font"):
            font = sys.argv[2]
            # Check if the font is valid
            if font not in pyfiglet.FigletFont.getFonts():
                sys.exit(f"Invalid font name: {font}")
        else:
            sys.exit("Invalid argument: --random or -f/--font <fontname>")
    except IndexError:
        font = "big"  # Default font if no arguments are given

    print(f"Using font: {font}")  # Display the chosen font

    print("1. Pomodoro")
    print("2. Long Break")
    print("3. Short Break")
    print("4. Custom Duration")
    print("5. Options")

    try:
        choice = int(input("Option: "))
        match choice:
            case 1:
                timer_custom(font, 25)
            case 2:
                timer_custom(font, 10)
            case 3:
                timer_custom(font, 5)
            case 4:
                timer_custom(font, int(input("Duration (mins): ")))
            case 5:
                auto_break = options()
                if auto_break:
                    try:
                        print("Cancel auto mode with Ctrl+C")
                        timer_custom(font, 25)
                        timer_custom(font, 10)
                    except KeyboardInterrupt:
                        clear_stdout()
                        print("Auto mode canceled")
                        main()
            case _:
                print("Valid options are: 1, 2, 3, 4")
    except ValueError:
        print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()
