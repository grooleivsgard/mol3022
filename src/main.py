import tkinter as tk
from tkinter import ttk
from event_handlers import handle_submit, exit_program

# Fields for the form
fields = ('Transcription Factor - Matrix ID', 'Genome Sequence - GenBank Accession Number', 'Email')

# Function to create the form
def makeform(root, fields):
    entries = []
    for field in fields:
        # Frame
        frame = ttk.Frame(root)
        frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

        # Label
        lab = ttk.Label(frame, text=field, anchor='w')
        lab.pack(side=tk.TOP, fill=tk.X)

        # Entry
        ent = ttk.Entry(frame)
        ent.pack(side=tk.TOP, expand=tk.YES, fill=tk.X)

        # Error 
        error_label = ttk.Label(frame, text="", foreground='red')
        error_label.pack(side=tk.TOP, fill=tk.X)  

        entries.append((field, ent, error_label))
    return entries

def clear_entries(entries):
    for entry in entries:
        entry[1].delete(0, tk.END)  # Delete text from entry widget
        entry[2].config(text="")    # Clear error message, if any

if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()

    # Styling
    style = ttk.Style()
    style.theme_use('clam') # 'clam', 'alt', 'default', 'classic'

    # Title Label
    title_label = ttk.Label(root, text="Genome Analysis Tool", font=('Helvetica', 16, 'bold'), padding="10 10 10 0")
    title_label.pack(side=tk.TOP, fill=tk.X)

    # Description Label
    description_label = ttk.Label(root, text="This program allows you to analyze genomic sequences by providing a Transcription Factor Matrix ID from JASPAR, Genome Sequence Accession Number from NCBI, and your email for NCBI database access.", padding="10 10 10 10")
    description_label.pack(side=tk.TOP, fill=tk.X)

    ents = makeform(root, fields)

    # Placeholder for the PWM output label
    output_pwm = ttk.Label(root, text="")
    output_pwm.pack()

    output_score = ttk.Label(root, text="")
    output_score.pack()

    # Add a submit button
    b1 = ttk.Button(root, text="Submit", command=lambda: handle_submit(ents, output_pwm, output_score, root))
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    
    # Add a quit button
    b2 = ttk.Button(root, text="Quit", command=lambda: exit_program(root))
    b2.pack(side=tk.LEFT, padx=5, pady=5)

    # Add a clear button
    b3 = ttk.Button(root, text="Clear", command=lambda: clear_entries(ents))
    b3.pack(side=tk.LEFT, padx=5, pady=5)

    root.mainloop()



