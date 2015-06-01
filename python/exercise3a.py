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