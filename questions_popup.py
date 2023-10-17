import csv
import tkinter as tk
from tkinter import simpledialog

def ask_questions():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # List of questions
    questions = ["What is your name?", "How old are you?", "What's your favorite color?"]

    # Get answers
    answers = [simpledialog.askstring("Input", q) for q in questions]

    return answers

def write_to_csv(answers):
    with open("answers.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(answers)

def main():
    answers = ask_questions()
    write_to_csv(answers)

if __name__ == "__main__":
    main()
