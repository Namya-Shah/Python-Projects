# Python project to convert a book into an audiobook

import pyttsx3

book = open("book.txt", "r")

book_text = book.readlines()

engine = pyttsx3.init()

for i in book_text:
    engine.say()
    engine.runAndWait()