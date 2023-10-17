# task scheduled on windows 10 under Questionnaire GUI
import os
import csv
import tkinter as tk
from tkinter import simpledialog, messagebox
from datetime import datetime

if 'WSLENV' not in os.environ and os.name == 'nt':
    # Running on native Windows (not in WSL)
    import ctypes
    ctypes.windll.shcore.SetProcessDpiAwareness(1)

FILE_NAME = "activity_log.csv"

script_directory = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_directory, FILE_NAME)




class CustomSimpleDialog(simpledialog._QueryString):

    def body(self, master):
        # Removed the line that was causing the error

        label = tk.Label(master,
                         text=self.prompt,
                         font='Arial 18',
                         wraplength=400)
        label.pack(padx=5, pady=5)

        self.entry = tk.Entry(master, font='Arial 18')
        self.entry.pack(padx=5, pady=5)
        self.entry.bind("<Return>", self.ok)
        self.entry.focus_set()


def custom_ask_string(title, prompt):
    d = CustomSimpleDialog(title=title, prompt=prompt)
    return d.result


def get_last_planned_activity():
    if not os.path.exists(csv_path):
        return None

    with open(csv_path, "r", newline='') as file:
        reader = csv.reader(file)
        last_line = None
        for row in reader:
            last_line = row

    if last_line:
        return last_line[2]
    return None


def ask_questions():
    root = tk.Tk()
    root.withdraw()

    current_time_display = datetime.now().strftime('%d/%m %A %I:%M%p')
    planned_last_hour = get_last_planned_activity()

    if planned_last_hour:
        past_activity = custom_ask_string(
            "Activity Check",
            f"{current_time_display}\n\nWhat did you do in the last hour? (You planned: {planned_last_hour})"
        )
    else:
        past_activity = custom_ask_string(
            "Activity Check",
            f"{current_time_display}\n\nWhat did you do in the last hour?")

    next_activity = custom_ask_string(
        "Activity Planning",
        f"{current_time_display}\n\nWhat's your plan for the next hour?")

    root.destroy()
    return past_activity, next_activity


def main():
    past_activity, next_activity = ask_questions()

    # If either of the entries is blank, exit without writing to the CSV
    if not past_activity or not next_activity:
        return

    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(csv_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([current_time, past_activity, next_activity])


if __name__ == "__main__":
    main()
