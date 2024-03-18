from pyjaspar import jaspardb

class JASPARMotifAnalyzer:
    def __init__(self, release='JASPAR2024'):
        self.jdb_obj = jaspardb(release=release)

    # Get the motif PFM from JASPAR
    def get_motif_pfm(self, motif):
        # check if m