#!/usr/local/bin/python3

import json
import pathlib
import subprocess
import sys
import tkinter as tk
from tkinter import ttk


class CrunchFitnessBotInterface:
    def __init__(self, root):
        """
        Initialize the bot interface with the appropriate properties

        Keyword arguments:
        root -- the top-level window
        """

        self.root = root
        self.email_entry = ""
        self.crunch_password_entry = ""
        self.email_password_entry = ""
        self.times = {
            "Monday": "",
            "Tuesday": "",
            "Wednesday": "",
            "Thursday": "",
            "Friday": "",
            "Saturday": "",
            "Sunday": ""
        }
        self.root.resizable(False, False)
        canvas = tk.Canvas(self.root, height=500, width=600, bg="#F57F2B")
        canvas.pack()

    def create_email(self):
        """
        Create textbox for email entry 
        """

        email_label_frame = tk.Frame(self.root, bg="#F57F2B")
        email_label_frame.place(
            relx=0.5, rely=0.075, relwidth=0.75, relheight=0.075, anchor='n'
        )

        email_label = tk.Label(
            email_label_frame, font=("Helvetica", 14), text="Email", bg="#F57F2B", fg="#FFF"
        )
        email_label.place(relwidth=1, relheight=1)

        email_entry_frame = tk.Frame(self.root)
        email_entry_frame.place(
            relx=0.5, rely=0.15, relwidth=0.75, relheight=0.075, anchor='n'
        )

        email_var = tk.StringVar()

        self.email_entry = tk.Entry(
            email_entry_frame, textvariable=email_var, font=(
                "Helvetica", 16)
        )
        self.email_entry.place(relwidth=1, relheight=1)

    def create_email_password(self):
        """
        Create textbox for email password
        """

        email_password_label_frame = tk.Frame(self.root, bg="#F57F2B")
        email_password_label_frame.place(
            relx=0.5, rely=0.25, relwidth=0.75, relheight=0.075, anchor='n'
        )

        email_password_label = tk.Label(email_password_label_frame,
                                        font=("Helvetica", 14), text="Email Password", bg="#F57F2B", fg="#FFF"
                                        )
        email_password_label.place(relwidth=1, relheight=1)

        email_password_entry_frame = tk.Frame(self.root)
        email_password_entry_frame.place(
            relx=0.5, rely=0.325, relwidth=0.75, relheight=0.075, anchor='n'
        )

        email_password_var = tk.StringVar()

        self.email_password_entry = tk.Entry(
            email_password_entry_frame, textvariable=email_password_var, font=("Helvetica", 16), show="*"
        )
        self.email_password_entry.place(relwidth=1, relheight=1)

    def create_crunch_password(self):
        """
        Create textbox for Crunch Fitness password
        """

        crunch_password_label_frame = tk.Frame(self.root, bg="#F57F2B")
        crunch_password_label_frame.place(
            relx=0.5, rely=0.425, relwidth=0.75, relheight=0.075, anchor='n'
        )

        crunch_password_label = tk.Label(crunch_password_label_frame,
                                         font=("Helvetica", 14), text="Crunch Fitness Password", bg="#F57F2B", fg="#FFF"
                                         )
        crunch_password_label.place(relwidth=1, relheight=1)

        crunch_password_entry_frame = tk.Frame(self.root)
        crunch_password_entry_frame.place(
            relx=0.5, rely=0.5, relwidth=0.75, relheight=0.075, anchor='n'
        )

        crunch_password_var = tk.StringVar()

        self.crunch_password_entry = tk.Entry(
            crunch_password_entry_frame, textvariable=crunch_password_var, font=("Helvetica", 16), show="*"
        )
        self.crunch_password_entry.place(relwidth=1, relheight=1)

    def create_time_slots(self):
        """
        Create dropdrown for available timeslots
        """

        day_time_frame = tk.Frame(self.root, bg="#F57F2B")
        day_time_frame.place(relx=0.5, rely=0.65,
                             relwidth=0.75, relheight=0.1, anchor='n')

        mon_label = tk.Label(day_time_frame, font=("Helvetica", 16),
                             text="Mon", bg="#F57F2B", fg="#FFF")
        mon_label.place(relwidth=(1/7), relheight=0.5)

        tue_label = tk.Label(day_time_frame, font=("Helvetica", 16),
                             text="Tue", bg="#F57F2B", fg="#FFF")
        tue_label.place(relx=(1/7), relwidth=(1/7), relheight=0.5)

        wed_label = tk.Label(day_time_frame, font=("Helvetica", 16),
                             text="Wed", bg="#F57F2B", fg="#FFF")
        wed_label.place(relx=(1/7) * 2, relwidth=(1/7), relheight=0.5)

        thu_label = tk.Label(day_time_frame, font=("Helvetica", 16),
                             text="Thu", bg="#F57F2B", fg="#FFF")
        thu_label.place(relx=(1/7) * 3, relwidth=(1/7), relheight=0.5)

        fri_label = tk.Label(day_time_frame, font=("Helvetica", 16),
                             text="Fri", bg="#F57F2B", fg="#FFF")
        fri_label.place(relx=(1/7) * 4, relwidth=(1/7), relheight=0.5)

        sat_label = tk.Label(day_time_frame, font=("Helvetica", 16),
                             text="Sat", bg="#F57F2B", fg="#FFF")
        sat_label.place(relx=(1/7) * 5, relwidth=(1/7), relheight=0.5)

        sun_label = tk.Label(day_time_frame, font=("Helvetica", 16),
                             text="Sun", bg="#F57F2B", fg="#FFF")
        sun_label.place(relx=(1/7) * 6, relwidth=(1/7), relheight=0.5)

        weekday_timings = []

        # Display only hours of operations
        for i in range(5, 24):
            weekday_timings.append(
                f"0{i}:00"
            ) if i <= 9 else weekday_timings.append(
                f"{i}:00"
            )

        # Weekend timings are a subset of weekday timings
        weekend_timings = weekday_timings[2:14]

        self.times["Monday"] = ttk.Combobox(
            day_time_frame, values=weekday_timings, font="Helvetica"
        )
        self.times["Monday"].place(rely=0.5, relwidth=(1/7))

        self.times["Tuesday"] = ttk.Combobox(
            day_time_frame, values=weekday_timings, font="Helvetica"
        )
        self.times["Tuesday"].place(relx=(1/7), rely=0.5, relwidth=(1/7))

        self.times["Wednesday"] = ttk.Combobox(
            day_time_frame, values=weekday_timings, font="Helvetica"
        )
        self.times["Wednesday"].place(relx=(1/7) * 2, rely=0.5, relwidth=(1/7))

        self.times["Thursday"] = ttk.Combobox(
            day_time_frame, values=weekday_timings, font="Helvetica"
        )
        self.times["Thursday"].place(relx=(1/7) * 3, rely=0.5, relwidth=(1/7))

        self.times["Friday"] = ttk.Combobox(
            day_time_frame, values=weekday_timings, font="Helvetica"
        )
        self.times["Friday"].place(relx=(1/7) * 4, rely=0.5, relwidth=(1/7))

        self.times["Saturday"] = ttk.Combobox(
            day_time_frame, values=weekend_timings, font="Helvetica"
        )
        self.times["Saturday"].place(relx=(1/7) * 5, rely=0.5, relwidth=(1/7))

        self.times["Sunday"] = ttk.Combobox(
            day_time_frame, values=weekend_timings, font="Helvetica"
        )
        self.times["Sunday"].place(relx=(1/7) * 6, rely=0.5, relwidth=(1/7))

    def create_submission(self):
        """
        Create submit button
        """

        submit_button_frame = tk.Frame(self.root)
        submit_button_frame.place(
            relx=0.5, rely=0.85, relwidth=0.75, relheight=0.075, anchor='n'
        )

        submit_button = tk.Button(
            submit_button_frame, text="SUBMIT", font=("Helvetica", 16), bg="#D10224", command=self.run_app
        )
        submit_button.place(relwidth=1, relheight=1)

    def run_app(self):
        """
        Spawn a new process to perform the reservations
        """

        for day, time in self.times.items():
            selected_time = time.get()
            self.times[day] = selected_time

        # Update file path based on the runtime environment
        if getattr(sys, 'frozen', False):
            main_path = f"{sys._MEIPASS}/main.py"
        else:
            main_path = f"{pathlib.Path(__file__).parent.absolute()}/main.py"

        subprocess.Popen(['python3', main_path,
                          self.email_entry.get(), self.email_password_entry.get(), self.crunch_password_entry.get(), json.dumps(self.times)]
                         )

        self.root.destroy()

    def main(self):
        """
        Create the user interface
        """

        try:
            CrunchFitnessBotInterface.create_email(self)
            CrunchFitnessBotInterface.create_email_password(self)
            CrunchFitnessBotInterface.create_crunch_password(self)
            CrunchFitnessBotInterface.create_time_slots(self)
            CrunchFitnessBotInterface.create_submission(self)
        except:
            print("The interface encountered an unexpected error")


if __name__ == "__main__":
    root = tk.Tk()
    interface = CrunchFitnessBotInterface(root)
    interface.main()
    root.mainloop()
