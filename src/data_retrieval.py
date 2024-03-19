from pyjaspar import jaspardb
from Bio import SeqIO
import numpy as np


"""
Get the motif PFM of a transcription factor from JASPAR and convert it to PWM.

Transcription factors are proteins that help turn 
specific genes on or off by binding to nearby DNA. 

A Position Weight Matrix (PWM) is a tool used to 
represent the binding preference of a transcription 
factor to DNA. Essentially, it's a table that helps 
predict where in the DNA this transcription factor might bind.

E.g. get the Probability Frequency Matrix (PFM) for PDX1 (a transcriptional activator of several genes, incl insulin)
"""

class MotifAnalyzer:
    def __init__(self, release='JASPAR2024'):
        self.jdb_obj = jaspardb(release=release)

    def get_motif_pwm(self, motif):
        # check if motif is the motif name or the motif ID
        if motif.startswith('MA'):
            pwm = self.jdb_obj.fetch_motif_by_id(motif).pwm
            print(pwm)  # For debugging
            return pwm
        else:
            pwm = self.jdb_obj.fetch_motifs_by_name(motif).pwm  # doesn't work
            print(pwm)
            return pwm

"""
Idenitfy a DNA sequence that is a target gene of the transcription factor.
These regions are often found in the promoter regions of genes 
(the part of the gene located at the start of the gene, controlling its transcription).

Then, import a FASTA file of a DNA sequence to convert it to a list of sequences.

TODO: Implement access to NCBIs Entrez databases (https://biopython.org/DIST/docs/tutorial/Tutorial.html#sec197, ch. 10)
"""
class SequenceParser:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_fasta(self):
        # Reads a FASTA file and returns a list of sequences.
        sequences = []
        for record in SeqIO.parse(self.file_path, "fasta"):
            sequences.append(str(record.seq).upper())
        return sequences

