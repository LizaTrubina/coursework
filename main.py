import sys
from pageRank import pageRank

links = [[]]

def read_file():
   # filename = os.path.join(os.path.dirname(__file__), 't.txt')
    f = open("t.txt", 'r')
    for line in f:
        (frm, to) = map(int, line.split(" "))
        extend = max(frm - len(links), to - len(links)) + 1
        for i in range(extend):
            links.append([])
        links[frm].append(to)
    f.close()

read_file()

pr =  pageRank(links, alpha=0.85, convergence=0.00001, checkSteps=10)
sum = 0
for i in range(len(pr)):
    print(i, "=", pr[i])
    sum = sum + pr[i]
print("s = " + str(sum))
