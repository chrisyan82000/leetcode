def stringCompression(chars):
    letptr = 0
    numptr = 0
    
    while letptr < len(chars):
        char = chars[letptr] 
        freq = 0
        while letptr < len(chars) and chars[letptr] == char:
            letptr += 1
            freq += 1
        chars[numptr] = char
        numptr += 1
        if freq > 1:
            for i in str(freq):
                chars[numptr] = i
                numptr += 1
    return numptr
