def solution(s):
    pares = [s[c:c+2] for c in range(0, len(s)-1,2)]
    if len(s)%2!=0:
        pares.append(s[-1]+ "_")
    
    return pares