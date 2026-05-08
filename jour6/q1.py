def solution(a):
    n = len(a)
    b = [0] * n
    for i in range(n):
        gauche = a[i-1] if i > 0 else 0
        centre = a[i]
        droite = a[i+1] if i < n-1 else 0
        b[i] = gauche + centre + droite
    return b