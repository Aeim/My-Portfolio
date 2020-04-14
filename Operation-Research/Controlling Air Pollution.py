from pulp import *
problem = LpProblem("Controlling Air Pollution", LpMinimize)

# Create Variables
num_abate = 6
x = LpVariable.dicts("x",list(range(num_abate)),0 , 1) # x >= 0
annual_cost = [8,10,7,6,11,9]
reduct_req = [60,150,125]
emiss_rate = [[12,9,25,20,17,13],
              [35,42,18,31,56,49],
              [37,53,28,24,29,20]]            


# Objective Function
problem += lpSum([annual_cost[i] * x[i] for i in range(num_abate)])

# Constraint
c1 = lpSum([emiss_rate[0][j] * x[j] for j in range(len(emiss_rate[0]))]) >= reduct_req[0]
c2 = lpSum([emiss_rate[1][j] * x[j] for j in range(len(emiss_rate[1]))]) >= reduct_req[1]
c3 = lpSum([emiss_rate[2][j] * x[j] for j in range(len(emiss_rate[2]))]) >= reduct_req[2]


problem += c1
problem += c2
problem += c3

print(problem)
problem.solve()
print(value(problem.objective))
for i in range(num_abate) :
    print(value(x[i]))