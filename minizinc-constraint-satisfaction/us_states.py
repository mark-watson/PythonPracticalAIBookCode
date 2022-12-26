from minizinc import Instance, Model, Solver

coinbc = Solver.lookup("coinbc")

model = Model("./us_states.mzn")
instance = Instance(coinbc, model)
instance["nc"] = 4  # solve for a maximum of 4 colors

result = instance.solve()
print(result)
all_states = list(result.__dict__["solution"].__dict__.keys())
all_states.remove("_checker")
print(all_states)
for state in all_states:
    print(f" {state} \t: \t{result[state]}")
