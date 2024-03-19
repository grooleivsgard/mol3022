from calculations import scan_sequence, plot_scores
from data_retrieval import MotifAnalyzer, SequenceParser

# Example: 
filename = "data/sequence.fasta" # Example fasta file
threshold = 0.5  # Example threshold
motif = "MA0132.2"  # Example motif

if __name__ == "__main__":
    pwm = MotifAnalyzer().get_motif_pwm(motif)
    dna_sequence = SequenceParser(filename).read_fasta()
    # Scan the sequence
    potential_sites, scores = scan_sequence(pwm, dna_sequence, threshold)
    # Visualize results
    plot_scores(scores, threshold)

