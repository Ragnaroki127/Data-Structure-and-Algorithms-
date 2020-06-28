# python3
import itertools
n, m = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(m) ]

# This solution prints a simple satisfiable formula
# and passes about half of the tests.
# Change this function to solve the problem.
i_range = range(1, n + 1)
j_range = range(1, 4)

clauses = []

def var_num(i, j):
    assert(i in i_range and j in j_range)
    return (i - 1) * 3 + j

def exactly_one_of(literals):
    clauses.append([l for l in literals])
    for pair in itertools.combinations(literals, 2):
        clauses.append([-l for l in pair])
def different_color(x, y):
    for i, j in zip(x, y):
        clauses.append([-i, -j])

def printEquisatisfiableSatFormula():
    for i in i_range:
        exactly_one_of([var_num(i, j) for j in j_range])
    for i1, i2 in edges:
        x = [var_num(i1, j) for j in j_range]
        y = [var_num(i2, j) for j in j_range]
        different_color(x, y)

    print('{} {}'.format(len(clauses), n * 3))
    for clause in clauses:
        clause.append(0)
        print(" ".join(map(str, clause)))
    '''
    with open('solution.cnf', 'w') as f:
        f.write('p cnf {} {}'.format(n * 3, len(clauses)))
        for clause in clauses:
            f.write("\n" + " ".join(map(str, clause)))
    '''
printEquisatisfiableSatFormula()
