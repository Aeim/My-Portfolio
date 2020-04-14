from pulp import *
problem = LpProblem("Region Planing", LpMaximize)

# Create Variables
num_quan = 9
xj = LpVariable.dicts("x",list(range(num_quan)) , 0) # x >= 0

# Objective Function
problem += 1000*(xj[0]+xj[1]+xj[2]) + 750*(xj[3]+xj[4]+xj[5]) + 250*(xj[6]+xj[7]+xj[8])

# Constraint
c1 = xj[0] + xj[3] + xj[6] <= 400
c2 = xj[1] + xj[4] + xj[7] <= 600
c3 = xj[2] + xj[5] + xj[8] <= 300

c4 = 3*xj[0] + 2*xj[3] + xj[6] <= 600
c5 = 3*xj[1] + 2*xj[4] + xj[7] <= 800
c6 = 3*xj[2] + 2*xj[5] + xj[8] <= 375

c7 = xj[0] + xj[1] + xj[2] <= 600
c8 = xj[3] + xj[4] + xj[5] <= 500
c9 = xj[6] + xj[7] + xj[8] <= 325

c10 = 3*(xj[0]+xj[3]+xj[6]) - 2*(xj[1]+xj[4]+xj[7]) == 0
c11 = (xj[1]+xj[4]+xj[7])   - 2*(xj[2]+xj[5]+xj[8]) == 0
c12 = 4*(xj[2]+xj[5]+xj[8]) - 3*(xj[0]+xj[3]+xj[6]) == 0

problem += c1
problem += c2
problem += c3
problem += c4
problem += c5
problem += c6
problem += c7
problem += c8
problem += c9
problem += c10
problem += c11
problem += c12

print(problem)
problem.solve()
print(value(problem.objective))