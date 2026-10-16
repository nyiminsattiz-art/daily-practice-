def get_length_of_missing_array(array_of_arrays):
    if not array_of_arrays:
        return 0
    
    try:
        sorted_arrays = sorted(array_of_arrays, key=len);
    except TypeError:
        return 0
    
    for array in sorted_arrays:
        if array == None or len(array) == 0:
            return 0
        
    expected_length = len(sorted_arrays[0])
    
    for arr in sorted_arrays:
        if len(arr) != expected_length:
            return expected_length
        expected_length += 1
