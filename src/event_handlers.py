from calculations import scan_sequence
from data_retrieval import fetch_motif_pwm, fetch_sequence
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import itertools


# NOT FINISHED
def validate(entries):
    # Function to validate the input
    valid = True

    for field, entry in entries:
        text = entry.get().strip()  # Remove leading/trailing whitespaces
        if not text:  # Basic check for non-empty
            print(f"Error: {field} is required.")
            valid = False
            continue  # Add more specific checks as needed
        
        # Example: specific field validation
        if field == 'Email' and '@' not in text:
            print(f"Error: {field} doesn't seem to be a valid email.")
            valid = False
    return valid


def handle_submit(entries, output_pwm, root):
    
    # Function to handle the submit button click
    pwm_id, ncbi_id, email = [entry[1].get().strip() for entry in entries]

    # Fetch the PWM
    pwm = fetch_motif_pwm(pwm_id)
    output_pwm.config(text=f"{pwm}")

    # Fetch the DNA sequence
    dna_sequence = fetch_sequence(ncbi_id, email)

    # Scan the DNA sequence for potential binding sites
    scores, binding_site = scan_sequence(pwm, dna_sequence)

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

    for i, score in enumerate(scores):
        ax.plot(score, label=f'score {i + 1}', color=next(colors))

    ax.set_title('Transcription Factor Binding Sites')
    ax.set_xlabel('Position in the DNA sequence')
    ax.set_ylabel('PWM Score')
    ax.legend()

    # Convert binding_site list to string
    binding_site_str = ''.join(binding_site)
    # Find index of maximum score
    max_score_index = max(range(len(scores[0])), key=lambda x: scores[0][x])
    # Annotate the top of the plot with the binding site string
    ax.annotate(binding_site_str, xy=(max_score_index, max(scores[0])), xytext=(max_score_index, max(scores[0]) + 0.05),
                arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=12)

    return fig


def exit_program(root):
    root.destroy()  # Avslutter GUI-vinduet og dermed programmet
