import tkinter as tk
from tkinter import ttk
from event_handlers import handle_submit
from event_handlers import exit_program
import sys

if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()
    root.title("Identify the most likely transcription factor binding sites in the DNA sequence")

    # Create an input field where the user can enter data
    input_label = tk.Label(root, text="Enter your Matrix ID:")
    input_label.pack()

    # Create an input field where the user can enter data
    entry = tk.Entry(root)
    entry.pack()
    # Create a button to submit the data
    submit_button = tk.Button(root, text="Submit", command=lambda: handle_submit(entry, pwm_output, root))
    submit_button.pack()

    # Create a label to display the PWM output
    pwm_output = tk.Label(root, text="")
    pwm_output.pack()

    # Create a button to exit the program
    exit_button = tk.Button(root, text="Exit", command=sys.exit)
    exit_button.pack()

    # Start the main loop
    root.mainloop()