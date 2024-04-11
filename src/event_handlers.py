from calculations import scan_sequence
from data_retrieval import fetch_motif_pwm, fetch_sequence
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import itertools
import re
import sys


# Function to validate the input
def validate(entries):
    errors = {}

    for field, entry, _ in entries:
        text = entry.get().strip()  # Remove leading/trailing whitespaces
        
        # Basic check for non-empty fields
        if not text:  
            errors[field] = "This field is required."
        
        # Transcription Factor - Matrix ID validation - either 'MA' or 'UN' followed by a number and a dot and another number
        if field == 'Transcription Factor - Matrix ID' and not re.match(r'^(MA|UN)\d\.\d$', text):
            errors[field] = "Must start with 'MA' or 'UN', followed by a version number (e.g. MA1636.1)."
        
        # Genome Sequence Accession 
        if field == 'Genome Sequence - GenBank Accession Number' and not re.match(r"^[A-Za-z]{1,2}\d{5,}\.\d$", text):
            errors[field] = "Must start with one or two letters followed by at least five digits (e.g. M57671.1)."

        # E-mail validation
        if field == 'Email' and '@' not in text:
            errors[field] = "This doesn't seem to be a valid email."
    
    return errors


def handle_submit(entries, output_pwm, output_score, root):
    field_errors = validate(entries)

    # Reset the error labels for all fields
    for _, _, error_label in entries:
        error_label.config(text='')

    # Check if there are any errors and display them
    if field_errors:
        for field, entry, error_label in entries:
            if field in field_errors:
                error_label.config(text=field_errors[field], foreground='red')
        return # Stop the function since there are errors

    for _, _, error_label in entries:
        error_label.config(text='')

    # Function to handle the submit button click
    pwm_id, ncbi_id, email = [entry[1].get().strip() for entry in entries]

    # Fetch the PWM
    pwm = fetch_motif_pwm(pwm_id)
    output_pwm.config(text=f"{pwm}")

    # Fetch the DNA sequence
    dna_sequence = fetch_sequence(ncbi_id, email)

    # Scan the DNA sequence for potential binding sites
    scores, binding_site, max_score = scan_sequence(pwm, dna_sequence)
    output_score.config(text=f"PWM score for best binding site: {max_score}")

    # Plot scores
    fig = plot_scores(scores, binding_site, root)
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()

# Function to plot the scores
def plot_scores(scores, binding_site, root):

    fig, ax = plt.subplots(figsize=(10, 6))
    colors = itertools.cycle(['blue', 'green', 'red'])  # Use a cyclic color palette

    max_score = 0
    max_index = 0
    for i, score in enumerate(scores):
        ax.plot(score, label=f'score {i + 1}', color=next(colors))
        if (max_score < max(score)):
            max_score_index = max(range(len(scores[i])), key=lambda x: scores[i][x])
            max_index = i
            max_score = max(score)

    ax.set_title('Transcription Factor Binding Sites')
    ax.set_xlabel('Position in the DNA sequence')
    ax.set_ylabel('PWM Score')
    ax.legend()

    # Convert binding_site list to string
    binding_site_str = ''.join(binding_site)
    # Find index of maximum score


    # Annotate the top of the plot with the binding site string
    ax.annotate(binding_site_str, xy=(max_score_index, max(scores[max_index])), xytext=(max_score_index, max(scores[max_index]) + 0.05),
                arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12)

    return fig


def exit_program(root):
    root.destroy()  # Ends the GUI window / the program
    sys.exit()

def clear_entries(entries):
    for entry in entries:
        entry[1].delete(0, ttk.END)  # Delete text from entry widget
        entry[2].config(text="")    # Clear error message, if any
