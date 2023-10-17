import csv
import tkinter as tk
from tkinter import simpledialog, messagebox
from datetime import datetime
import os

FILE_NAME = "activities.csv"

def get_last_planned_activity():
    if not os.path.exists(FILE_NAME):
        return None

    with open(FILE_NAME, "r", newline='') as file:
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
        past_activity = simpledialog.askstring("Activity Check", f"{current_time_display}\n\nWhat did you do in the last hour? (You planned: {planned_last_hour})")
    else:
        past_activity = simpledialog.askstring("Activity Check", f"{current_time_display}\n\nWhat did you do in the last hour?")

    next_activity = simpledialog.askstring("Activity Planning", f"{current_time_display}\n\nWhat's your plan for the next hour?")

    root.destroy()
    return past_activity, next_activity

def main():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    past_activity, next_activity = ask_questions()

    with open(FILE_NAME, "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([current_time, past_activity, next_activity])

if __name__ == "__main__":
    main()
