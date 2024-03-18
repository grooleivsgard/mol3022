from motif_analyzer import JASPARMotifAnalyzer

if __name__ == "__main__":
    # Example: get the Probability Frequency Matrix (PFM) for PDX1 (a transcriptional activator of several genes, incl insulin)
    analyzer = JASPARMotifAnalyzer()
    motif = analyzer.get_motif_pwm('MA0132.2')
    print(motif)

