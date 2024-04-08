import tkinter as tk
from tkinter import ttk
from event_handlers import handle_submit
from event_handlers import exit_program

# Fields for the form
fields = ('PWM', 'NCBI ID', 'Email')

# Function to fetch the values from the form
def fetch(entries):
        for entry in entries:
            field = entry[0]
            text  = entry[1].get()
            print('%s: "%s"' % (field, text))

# Function to create the form
def makeform(root, fields):
    entries = []
    for field in fields:
        row = tk.Frame(root)
        lab = tk.Label(row, width=15, text=field, anchor='w')
        ent = tk.Entry(row)
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        entries.append((field, ent))
    return entries
    
if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()
    ents = makeform(root, fields)

    # Placeholder for the PWM output label
    output_pwm = tk.Label(root, text="")
    output_pwm.pack()

    # Add a submit button
    b1 = tk.Button(root, text="Submit", command=lambda: handle_submit(ents, output_pwm, root))
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    
    # Add a quit button
    b2 = tk.Button(root, text="Quit", command=lambda: exit_program(root))
    b2.pack(side=tk.LEFT, padx=5, pady=5)

    root.mainloop()
