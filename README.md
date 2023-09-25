# Password Generator

A secure and customizable password generator that offers encrypted password outputs.

## Overview

This password generator is designed to create strong, random passwords based on user preferences. The user has the flexibility to choose the length of the password, as well as whether to include uppercase letters, digits, and special characters. One of the unique features is its ability to generate non-consecutive repeating characters in the password, enhancing its complexity.

Furthermore, users have the option to get the password in an encrypted format, making the storage of these passwords more secure. A separate decryption script (`decrypt.py`) is provided to retrieve the original password using the encryption key.

## Challenges Faced

- **Non-repeating Characters**: One of the primary challenges was ensuring that the generated passwords don't have consecutive repeating characters. This was achieved through iterative logic which checks the last character and ensures the next one is of a different type.
- **Fernet Encryption**: The integration of the Fernet encryption library was a new experience. Understanding and implementing encryption and decryption mechanisms was crucial for this project.
- **Encryption Key Handling**: Properly handling the encryption key was essential. The key, once generated, is displayed to the user without additional formatting characters, facilitating easier copy-pasting.

## Features

- User-defined password length.
- Options to include uppercase, digits, and special characters.
- Non-consecutive repeating characters in passwords.
- Password strength evaluation with visual emoji feedback.
- Option for encrypted password output.
- Separate decryption utility.

## Usage

1. Run the `main.py` script.
2. Follow the interactive prompts to specify your password preferences.
3. If encryption is chosen, securely store the displayed encryption key. You'll need this for decryption.
4. To decrypt an encrypted password, use the `decrypt.py` script and provide the encryption key.

## Dependencies

- Python 3.x
- `cryptography` library

## Copyright

© Donovan Townes, 2023  
Email: [z8phyr@hotmail.com](mailto:z8phyr@hotmail.com)
