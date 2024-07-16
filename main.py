import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', 
    '(': '-.--.', ')': '-.--.-', ' ': '/'
}

def encrypt(message):
    morse_code_message = []
    for char in message.upper():
        if char in MORSE_CODE_DICT:
            morse_code_message.append(MORSE_CODE_DICT[char])
            morse_code_message.append(' ')
        elif char == ' ':
            morse_code_message.append('/')
            morse_code_message.append(' ')
    return ''.join(morse_code_message).strip()

def decrypt(message):
    morse_code_dict_reversed = {value: key for key, value in MORSE_CODE_DICT.items()}
    words = message.split('/')
    decoded_message = []
    for word in words:
        decoded_word = ''.join(morse_code_dict_reversed[code] for code in word.split() if code in morse_code_dict_reversed)
        decoded_message.append(decoded_word)
    return ' '.join(decoded_message)

class MorseCodeApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Morse Code Encryptor/Decryptor')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.text_input = QLineEdit(self)
        self.text_input.setPlaceholderText('Enter text to encrypt or Morse code to decrypt')
        layout.addWidget(self.text_input)

        self.encrypt_button = QPushButton('Encrypt to Morse Code', self)
        self.encrypt_button.clicked.connect(self.encrypt_text)
        layout.addWidget(self.encrypt_button)

        self.decrypt_button = QPushButton('Decrypt from Morse Code', self)
        self.decrypt_button.clicked.connect(self.decrypt_text)
        layout.addWidget(self.decrypt_button)

        self.result_label = QLabel('Result:', self)
        layout.addWidget(self.result_label)

        self.result_text = QTextEdit(self)
        self.result_text.setReadOnly(True)
        layout.addWidget(self.result_text)

        self.setLayout(layout)

    def encrypt_text(self):
        text = self.text_input.text()
        encrypted_text = encrypt(text)
        self.result_text.setText(encrypted_text)

    def decrypt_text(self):
        morse_code = self.text_input.text()
        decrypted_text = decrypt(morse_code)
        self.result_text.setText(decrypted_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MorseCodeApp()
    ex.show()
    sys.exit(app.exec_())
