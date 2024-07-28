# Password-Manager
This Password Manager is a desktop application built with Python and Tkinter. It offers a user-friendly interface for generating secure passwords, saving account credentials, and retrieving stored passwords for various websites.

## Features
- Generate secure random passwords
- Save website credentials (website, email, password)
- Retrieve saved passwords
- Copy passwords to clipboard automatically
- User-friendly graphical interface

## Requirements
- Python 3.x
- Tkinter 
- pyperclip

## How It Works

### User Interface
The application uses Tkinter to create a GUI with input fields for website, email/username, and password, along with buttons for various functions and a logo display.

### Password Generation
- The `generator()` function creates random passwords using letters, numbers, and symbols.
- Generated passwords are automatically inserted into the password input field.

### Saving Passwords
- The `saved()` function collects input data, validates it, and saves it to a JSON file ("data_file.json").
- It performs basic validation and asks for user confirmation before saving.
- Saved passwords are automatically copied to the clipboard.

### Finding Passwords
- The `find_password()` function searches the JSON file for stored credentials based on the website name.
- If found, it displays the information and copies the password to the clipboard.

### Data Storage
- Credentials are stored in a JSON file, using the website as the key and containing nested email and password values.

### Error Handling
- The application handles scenarios like missing files or empty inputs, displaying appropriate messages to the user.

### Clipboard Integration
- Uses pyperclip to copy generated or retrieved passwords to the clipboard.

## File Structure
- `main.py`: The main application script
- `data_file.json`: JSON file for storing credentials
- `logo.png`: Logo image for the application GUI

## Contributing
Contributions, issues, and feature requests are welcome.
