"""
Use the PWM of the TF to scan through the DNA sequence. The purpose is to look for
sections of the DNA that match the pattern in the PWM because these are places
where the TF is likely to bind.
"""

# Scan a DNA sequence for potential binding sites using a PWM.
def scan_sequence(pwm, sequences):
    all_scores = []
    binding_sites = []
    max_score = 0

    # Calculate scores for the entire DNA sequence
    for sequence in sequences:
        score = calculate_pwm_score(pwm, sequence)
        all_scores.append(score)

    # Find max_score and corresponding index
    for j, score_list in enumerate(all_scores):
        for k in range(len(score_list) - len(pwm['A']) + 1):
            if score_list[k] > max_score:
                max_score = score_list[k]
                max_index = k
                max_seq = j

    # Find binding sites
    for i in range(len(pwm['A'])):
        binding_sites.append(sequences[max_seq][max_index + i])

    return all_scores, binding_sites, max_score


# Calculate the score for a sequence against a given PWM.
def calculate_pwm_score(PWM, sequence):
    scores = []
    for i in range(len(sequence) - len(PWM['A']) + 1):
        score = 0

        # Calculate the probability and score for each base in the sequence
        for j in range(len(PWM['A'])):
            base = sequence[i + j]
            
            # Check for ambiguous bases
            if base == 'K':
                base = 'A'
            if base == 'W':
                base = 'A'

            # Calculate the probability and score    
            if base in PWM:
                score += PWM[base][j]
            else:
                score = score

        scores.append(score)

    return scores
