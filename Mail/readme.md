# Mail Program

This code allows you to send an email with attachments using the Simple Mail Transfer Protocol (SMTP) in Python.

## Setup

Before running the code, ensure that you have the following requirements:

- Python: The code is written in Python, so make sure you have Python installed on your system.

## Usage

1. Importing Credentials:
   - Create a file named `creds.py` in the same directory as the code.
   - In `creds.py`, define two variables: `email` (your email address) and `password` (your email account password).
     ```python
     email = "your_email@gmail.com"
     password = "your_password"
     ```
   - Make sure to replace `"your_email@gmail.com"` with your actual email address and `"your_password"` with your email account password.

2. Replace empty strings in the code with appropriate values:
   - In the line `msg['Subject'] = ""`, specify the subject of the email.
   - In the line `files = ['']`, provide the filenames or paths of the files you want to attach to the email.

3. Specify the recipient(s):
   - In the line `msg['To'] = ', '.join(creds.receiver)`, replace `creds.receiver` with the list of email addresses to which you want to send the email. You can enter multiple recipients by separating the email addresses with commas.

4. Customizing the email content:
   - In the line `msg.set_content("")`, enter the content or body of the email within the double quotes.

5. Running the code:
   - Execute the code, and it will perform the following steps:
     - Create an `EmailMessage` object to represent the email.
     - Set the subject, sender, recipients, and content of the email.
     - Attach the specified files to the email.
     - Establish a secure connection with the SMTP server (Gmail SMTP server in this case) using SSL.
     - Authenticate the sender's email account using the provided credentials.
     - Send the email with the attached files.
     - Print "Success" to indicate that the email was sent successfully.

6. Note:
   - The code is currently set to work with Gmail's SMTP server (`smtp.gmail.com`), which uses SSL on port 465. If you're using a different email provider, you may need to modify the SMTP server and port accordingly.

Feel free to customize the code based on your specific requirements. You can modify the email subject, content, attachments, and even the SMTP server settings. Enjoy sending emails with attachments using Python!