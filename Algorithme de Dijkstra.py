from sys import stdin, stdout
input, print = stdin.readline, stdout.write
def entre(inp): return list(inp.split())


def dijkstra(maxi, calc):
    s, d = entre(input()), entre(input())
    d = [list(dx.split(":")) for dx in d]
    for v in s:
        cpt = 0
        for dn in d:
            if calc:
                maxi += int(dn[1])
            if v in dn[0]:
                seul = dn
                cpt += 1
        calc = True
        if cpt < 2:
            s.remove(v)
            if cpt == 1:
                d.remove(seul)
    un, nb = s[:], [0] + [maxi] * (len(s) - 1)
    while un != []:
        pr = maxi
        for sn in un:
            pr = min(pr, nb[s.index(sn)])
        sx = s[nb.index(pr)]
        for dx in d:
            s1, s2 = dx[0][0], dx[0][1]
            if sx == s1:
                nb[s.index(s2)] = min(nb[s.index(s2)], nb[s.index(s1)] + int(dx[1]))
            elif sx == s2:
                nb[s.index(s1)] = min(nb[s.index(s1)], nb[s.index(s2)] + int(dx[1]))
        un.remove(sx)
    return str(nb[-1])


print(dijkstra(0, False))
