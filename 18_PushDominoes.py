def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        force = 0
        forces = [0] * n
        for i in range (n):
            if dominoes[i] == 'R':
                force = n
            elif dominoes[i] == "L":
                force = 0
            else:
                force = max(force-1,0)
            forces[i] += force
        force = 0
        for i in range(n-1,-1,-1):
            if dominoes[i] == "R":
                force = 0
            elif dominoes[i] == "L":
                force = n
            else:
                force = max(force-1,0)
            forces[i] -= force
        res = []
        for f in forces:
            if f>0:
                res.append("R")
            elif f<0:
                res.append("L")
            else:
                res.append(".")
        return "".join(res)
dominoes = list(map(str,input().split()))
res = pushDominoes(dominoes)
print(*res)