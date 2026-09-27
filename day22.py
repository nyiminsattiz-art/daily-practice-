def code_for_same_protein(seq1,seq2):
    new_seq1 = []
    for i in range(0, len(seq1), 3):
        word1 = seq1[i : i + 3]
        new_seq1.append(word1)

    new_seq2 = []
    for j in range(0, len(seq2), 3):
        word2 = seq2[j : j + 3]
        new_seq2.append(word2)
        
    protein1 = ""
    
    for dna1 in new_seq1:
        protein1 += codons[dna1]
    
    protein2 = ""
    for dna2 in new_seq2:
        protein2 += codons[dna2]
        
    if protein1 == protein2:
        return True
    else:
        return False
