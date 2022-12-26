from minizinc import Instance, Model, Solver

coinbc = Solver.lookup("coinbc")

test1 = Model("./test1.mzn")
instance = Instance(coinbc, test1)
instance["n"] = 30
instance["m"] = 200

result = instance.solve()
print(result)
print(result["x"])
print(result["y"])
