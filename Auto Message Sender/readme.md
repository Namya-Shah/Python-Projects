# Auto Message Sender

This script allows you to automate sending repetitive messages using the PyAutoGUI library. It simulates keyboard input to type and send a specified message multiple times.

## Installation

To run this script, you need to have Python installed on your system. Additionally, you need to install the PyAutoGUI library. You can install it using the following command:

```
pip install pyautogui
```

## Usage

1. Run the script `auto_message_sender.py` using Python.
2. Enter the number of times you want to send the message when prompted with "Enter limit:".
3. Enter the message you want to send when prompted with "Enter message:".
4. After a delay of 5 seconds (to give you time to focus on the desired application), the script will begin typing and sending the message repeatedly.
5. The script will automatically press the "Enter" key after typing each message.
6. It will continue sending messages until it reaches the specified limit.

**Note:** Ensure that the application where you want to send the message is active and has the input focus before running the script.

## Example

```
Enter limit: 10
Enter message: Hello, world!
```

This will send the message "Hello, world!" ten times.

## Limitations and Precautions

- Be cautious when using this script, as it can automate repetitive actions that may violate terms of service or acceptable use policies.
- Use this script responsibly and only in scenarios where it is permitted and appropriate.
- Ensure that you have the necessary permissions to send messages in the targeted application.
- Be mindful of potential consequences, such as spamming or excessive use of system resources.

## Acknowledgments

- This script utilizes the PyAutoGUI library for simulating keyboard input and automating the message sending process.