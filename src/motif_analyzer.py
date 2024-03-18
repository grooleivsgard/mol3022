from pyjaspar import jaspardb

class JASPARMotifAnalyzer:
    def __init__(self, release='JASPAR2024'):
        self.jdb_obj = jaspardb(release=release)

    # Get the motif PFM from JASPAR
    def get_motif_pfm(self, motif):
        # check if motif is the motif name or the motif ID
        if motif.startswith('MA'):
            return self.jdb_obj.fetch_motif_by_id(motif)
        else:
            return self.jdb_obj.fetch_motifs_by_name(motif)

    # Get the motif PWM
    def get_motif_pwm(self, motif):
        return self.get_motif_pfm(motif).pwm