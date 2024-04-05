import matplotlib.pyplot as plt
import re
import itertools


"""
Use the PWM of the TF to scan through the DNA sequence. The purpose is to look for
sections of the DNA that match the pattern in the PWM because these are places
where the TF is likely to bind.
"""

# Scan a DNA sequence for potential binding sites using a PWM.
def scan_sequence(pwm, dna_sequence, threshold):
    all_probabilities = []
    all_scores = []
    for i, sequence in enumerate(dna_sequence):
    #print(sequence)
        probabilities, score = calculate_pwm_score(pwm, sequence)  # Calculate scores for the entire DNA sequence
        all_probabilities.append((probabilities))
        all_scores.append((score))
    potential_sites = []

    max_score = 0
    binding_sites = []
    index = 0
    for i in range(len(sequence)-len(pwm['A'])+1):
        if score[i] > max_score:
            max_score = score[i]
            index = i


   #         window = dna_sequence[i:i + len(pwm['A'])]  # Get the window corresponding to the score
   #         potential_sites.append((i, window))
    for j in range(len(pwm['A'])):
                    binding_sites.append(sequence[index+j])
    print(max_score)
    return all_probabilities, all_scores, binding_sites

# Calculate the score for a sequence against a given PWM.

def calculate_pwm_score(PWM, sequence):
    probabilities = []
    scores = []
    for i in range(len(sequence) - len(PWM['A']) + 1):
        probability = 1
        score = 0
        for j in range(len(PWM['A'])):
            base = sequence[i + j]
            #if base == 'K':
            #    base = 'A'
            #if base == 'W':
            #    base = 'A'
            if base in PWM:
                probability *= PWM[base][j]
                score += PWM[base][j]
            else:
                probability = 1
                score = score
        probabilities.append(probability*20)
        scores.append(score)
    return probabilities, scores



"""
Visualize the scores of the PWM along the DNA sequence.
"""

def plot_scores(probabilities, scores):
     fig, ax = plt.subplots(figsize=(10, 6))

     colors = itertools.cycle(['blue', 'green', 'red'])  # Use a cyclic color palette

     for i in scores:
         ax.plot(i, label='score')

     ax.set_title('Transcription Factor Binding Probability')
     ax.set_xlabel('Position in the DNA sequence')
     ax.set_ylabel('Probability and Score')
     ax.legend()

     return fig




