from pyjaspar import jaspardb
from Bio import Entrez, SeqIO
import re

# Fetch a motif from JASPAR and convert it to a PWM
def fetch_motif_pwm(motif, release='JASPAR2024'):
    
    print("Fetching motif...")
    jdb_obj = jaspardb(release=release)
    try:
        # Assuming fetch_motif_by_id is a method that returns a motif object with a pwm attribute
        pwm = jdb_obj.fetch_motif_by_id(motif).pwm
        print("Successfully fetched motif!")
    except AttributeError:
        print(f"Motif ID {motif} not found.")
        return None
    return pwm
    

# Fetch a DNA sequence in FASTA format from NCBI
def fetch_sequence(id, email):

    Entrez.email = email # Always tell NCBI who is accessing the database

    try:
        with Entrez.efetch(db="nucleotide", id=id, rettype="fasta", retmode="text") as handle:
            sequence_data = SeqIO.read(handle, "fasta")
            dna_sequence = str(sequence_data.seq)
            print("Successfully fetched dna sequence!")
        
        # Split the DNA sequence into separate sequences if there are any Ns
        split_sequences = re.split('N+', dna_sequence)
        split_sequences = [seq for seq in split_sequences if seq]

        print(f"Split sequences: {split_sequences}") # For debugging

        return split_sequences
    
    except Exception as e:
        print(f"Error fetching sequence: {e}")
        return None



