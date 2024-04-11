# Development and Implementation of a Tool for Identifying Transcription Factor Binding Sites in DNA Sequences

This project aims to develop a tool to identify transcription factor binding sites in DNA sequences. 
Transcription factors play a role in regulating gene expression, and understanding their binding sites can provide insights into gene regulation mechanisms.

## Features
- Identification of transcription factor binding sites using PWM (Position Weight Matrix) scores.
- Utilization of data from Jaspar database for transcription factor binding motifs.
- User-friendly interface for inputting DNA sequences and viewing results.
- Potential to explore gene regulation mechanisms associated with diseases like diabetes.

# Dependencies
- pip install biopython
- pip install pyjaspar
- pip install matplotlib

# How to Run

To run the program, execute the following command in your terminal:

python main.py

Once the GUI window appears, follow these steps:

- Enter the matrix ID from Jaspar and Genome Sequence GenBank Accession Number in the designated field.
- Provide your email address in the respective field.
- Click the "Submit" button to initiate the analysis.
- The program will process the input data and generate plots based on the analysis.

