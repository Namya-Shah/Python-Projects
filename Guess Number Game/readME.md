# Number Guessing Game

This code implements a simple number guessing game in Python. The program generates a random number between 1 and 100 and prompts the user to guess the number. The user is provided with feedback indicating whether their guess is higher or lower than the generated number until they guess correctly.

## Getting Started

1. Ensure that you have Python 3.x installed on your system.
2. Download the code and save it to a Python file, e.g., `number_guessing_game.py`.
3. Run the code using the command `python number_guessing_game.py`.

## Gameplay

1. Upon running the code, you will be prompted to guess a number between 1 and 100.
2. Enter your guess as an integer and press Enter.
3. The program will provide feedback based on your guess:
   - If your guess is higher than the generated number, you will be informed that you guessed a higher number.
   - If your guess is lower than the generated number, you will be informed that you guessed a lower number.
4. Repeat the guessing process until you guess the correct number.
5. Once you guess the correct number, the program will display "You did it!" and terminate.

## Customization

You can modify the code according to your preferences or requirements. Here are some possible modifications:

- Adjust the range of numbers by modifying the arguments of the `random.randrange()` function.
- Customize the prompt message by modifying the string passed to the `input()` function.
- Change the feedback messages for higher and lower guesses to your liking.
- Add additional functionality or features to enhance the game.

## Dependencies

The code relies on the following library:

- `random`: Used for generating random numbers.

## Note

- This code is a basic implementation and does not include advanced error handling or input validation.
