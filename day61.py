def fold_array(array, runs):
    for i in range(runs):
        folded = []
        n = len(array)
        
        for j in range(n // 2):
            folded.append(array[j] + array[n - 1 - j])
            
        if n % 2 != 0:
            folded.append(array[n // 2])
        
        array = folded
    return array
                
