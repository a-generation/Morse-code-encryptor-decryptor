# Morse code encryptor/decryptor

Morse Code Encryptor/Decryptor
This Python application with PyQt5 library allows users to encrypt text into Morse code and decrypt Morse code back into text.

Description
The program is a graphical application that enables you to:

Input text in English language to encrypt into Morse code.
Input Morse code to decrypt back into text.
Automatically insert "/" as a separator between words in the encrypted message.
## Installation
To run the application, you'll need Python 3.x and the PyQt5 package installed. Install PyQt5 using the following command:

```bash
pip install PyQt5
```
Usage
Run the main.py script:

```bash
python main.py
```
## Features
Encryption: Convert text (Latin characters) into Morse code.
Decryption: Convert Morse code back into readable text.
Graphical Interface: User-friendly interface with input fields and buttons for encryption and decryption.
## How It Works
Encryption: Each character in the input text is converted into its Morse code equivalent. Spaces between words are represented by "/".
Decryption: Morse code input is parsed to convert each sequence back into its corresponding character.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Built using Python and PyQt5.
Morse code dictionary includes only Latin characters.

