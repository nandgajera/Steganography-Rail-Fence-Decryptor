# 🕵️‍♂️ Image Steganography Decryptor (LSB + Rail Fence)

This project is a **simple web-based tool** that extracts hidden messages from images using **Least Significant Bit (LSB)** steganography and decrypts the text using the **Rail Fence Cipher**.

It is built for educational purposes to demonstrate how cryptography and steganography can be combined to hide and reveal secret messages.

---

## 🌐 Live Demo
Once GitHub Pages is enabled, your site will be available at:

https://nandgajera.github.io/Steganography-Rail-Fence-Decryptor/

## ⚙️ How It Works

1. The **Python script** encrypts a message using the **Rail Fence Cipher** and embeds it into an image using **LSB encoding**.
2. The **HTML web page** allows you to upload that image, enter the same number of rails, and view the decrypted hidden message.

---

## 🧩 Input Page
Below is an example of the input interface where the user uploads the image and enters the number of rails.

Steganography-Rail-Fence-Decryptor/blob/main/input.png

---

## 🖥️ Output Page
After decryption, the hidden message appears below the button.

Steganography-Rail-Fence-Decryptor/blob/main/output.png

---

## 🐍 Python Encryption Script
Use the companion Python script to create stego images:

python encrypt_stego.py


