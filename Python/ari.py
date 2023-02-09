""" Here is a python implementation to compute the ARI for a given text file: """

def compute_ari(file_path):
    with open(file_path, 'r') as f:
        text = f.read()
        
    characters = len(text)
    words = len(text.split())
    sentences = text.count('.') + text.count('!') + text.count('?')
    
    ari = 4.71 * (characters / words) + 0.5 * (words / sentences) - 21.43
    
    return ari