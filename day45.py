def only_duplicates(st):
    result = ""
    for word in st:
        if st.count(word) >= 2:
            result += word
    return result
