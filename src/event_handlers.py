from calculations import scan_sequence
from data_retrieval import MotifAnalyzer, SequenceParser
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import itertools

# Example:
filename = "data/sequence.fasta"  # Example fasta file
threshold = 0.5  # Example threshold

def handle_submit(entry, pwm_output, root):
    # Function to handle what happens when the user clicks the "Submit" button
    user_input = entry.get()  # Get the text entered by the user
    pwm = MotifAnalyzer().get_motif_pwm(user_input)
    pwm_output.config(text=f"{pwm}")

    # Read the DNA sequence
    dna_sequence = SequenceParser(filename).read_fasta()
    # Scan the sequence
    probabilities, scores, binding_site = scan_sequence(pwm, dna_sequence, threshold)
    print(binding_site)
    # Plot scores
    fig = plot_scores(scores, binding_site, root)
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()

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


def exit_program():
    root.destroy()  # Avslutter GUI-vinduet og dermed programmet
    sys.exit()