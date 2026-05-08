def solution(pattern, source):
    voyelles = set('aeiouy')
    len_p = len(pattern)
    len_s = len(source)
    if len_p > len_s:
        return 0
    
    count = 0
    for i in range(len_s - len_p + 1):
        correspond = True
        for j in range(len_p):
            caractere = source[i + j]
            if pattern[j] == '0':
                if caractere not in voyelles:
                    correspond = False
                    break
            else:  # pattern[j] == '1'
                if caractere in voyelles:
                    correspond = False
                    break
        if correspond:
            count += 1
    return count