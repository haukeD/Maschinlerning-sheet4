import matplotlib.pyplot as plt
import numpy as np

D = np.array([[2, 10], [2, 5], [8, 4], [5, 8], [7, 5], [6, 4], [1, 2], [4, 9]])

print "\\begin{table}[tch]"

print "\\resizebox{\textwidth}{!}{"

print "\\begin{tabular}{","|c" * (D.shape[0]+1), "|}"

print "\hline"

#print map(lambda i: "x".join(str(i)), range(D.shape[0]))

for i in range(-1, D.shape[0]):
    for j in range(-1, D.shape[0]):
        if i == -1:
            if j == -1:
                print "",
            else:
                print "& $x^{(" + str(j+1) + ")}$",
        else:
            if j == -1:
                print "$x^{(" + str(i+1) + ")}$",
            else:
                x_ij = D[i] - D[j]
                print "& $", np.sqrt(x_ij.dot(x_ij)), "$",
    print "\\\\"
    print "\\hline"

#out= D[0] - D[1]
#print out
#print np.sqrt(out.dot(out))

print "\\end{tabular}"
print "}"
print "\\end{table}"

plt.plot(D[:,0], D[:,1],'.')
plt.grid(b=True, which='both', color='0.65',linestyle='-')

plt.savefig('../3a1.pdf')

M = np.array([[7, 4], [4, 9], [1.5, 3.5]])
plt.plot(M[:,0], M[:,1],'ro')

plt.savefig('../3a2.pdf')

for i in range(D.shape[0]):
    p = M[0] - D[i]
    min_p_i = 0
    minL = np.sqrt(p.dot(p))
    for j in range(1, M.shape[0]):
        p = M[j] - D[i]
        minLNew = np.sqrt(p.dot(p))
        if minLNew < minL:
            minL = minLNew
            min_p_i = j
        #plt.plot([D[i, 0], M[min_p_i, 0]], [D[i, 1], M[min_p_i, 1]], '-')
plt.savefig('../3a3.pdf')