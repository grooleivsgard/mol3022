import matplotlib.pyplot as plt


"""
Use the PWM of the TF to scan through the DNA sequence. The purpose is to look for 
sections of the DNA that match the pattern in the PWM because these are places 
where the TF is likely to bind.
"""

# Scan a DNA sequence for potential binding sites using a PWM.
def scan_sequence(pwm, dna_sequence, threshold):
    window_size = len(pwm)
    potential_sites = []
    scores = []

    for i in range(len(dna_sequence) - window_size + 1):
        window = dna_sequence[i:i+window_size]
        score = calculate_pwm_score(pwm, window)
        scores.append(score)
        if score > threshold:
            potential_sites.append((i, window))
            
    return potential_sites, scores

# Calculate the score for a sequence against a given PWM.
def calculate_pwm_score(pwm, sequence):
    score = 0
    for i, nucleotide in enumerate(sequence): # Iterate over the sequence and PWM
        if nucleotide in 'ACGT': # Check if the nucleotide is valid
            score += pwm[i]['ACGT'.index(nucleotide)] # Add the score for the nucleotide
    return score

"""
Visualize the scores of the PWM along the DNA sequence.
"""
def plot_scores(scores, threshold):
    plt.figure(figsize=(20, 6))
    plt.plot(scores, label='PWM Score')
    plt.axhline(y=threshold, color='r', linestyle='--', label='Threshold')
    plt.xlabel('Position')
    plt.ylabel('Score')
    plt.title('PWM Scoring Along DNA Sequence')
    plt.legend()
    plt.show()