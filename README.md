# password-manager

Password Manager

This is a simple password manager I made in Python to learn about object-oriented programming, encryption, hashing, and file handling. It stores passwords securely and uses a master password to protect access to the vault.

Features

* Master password protection
* Password encryption using Fernet
* SHA-256 hashing for security
* Save and load passwords from a file
* Add, view, and delete saved passwords
* Object-oriented design using classes

Classes

PasswordManager

This is the main class of the program. It handles storing, loading, encrypting, and decrypting passwords. It also manages the password vault file and keeps everything organised.

PasswordEntry

This class represents a single saved password. It stores information such as the website, username, and password. Using a separate class makes the code easier to manage and expand in the future.

Why I Made This

I created this project to improve my Python skills and learn more about cybersecurity. It helped me practise working with classes, encryption, hashing, files, and user input while building something useful.

Disclaimer

This project was made for learning purposes and should not be used to store important real-world passwords without further security improvements.