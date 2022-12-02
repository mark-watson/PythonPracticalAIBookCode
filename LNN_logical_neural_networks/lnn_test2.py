from lnn import *

# construct the model from formulae
model = Model()
p1, p2 = Predicates("P1", "P2")
x = Variable("x")
AB = And(p1(x), p2(x))
model.add_knowledge(AB)

# add data to the model
model.add_data({
    p1: {
        "0": Fact.TRUE,
        "1": Fact.TRUE,
        '2': Fact.FALSE,
        '3': Fact.FALSE
    },
    p2: {
        '0': Fact.TRUE,
        '1': Fact.FALSE,
        '2': Fact.TRUE,
        '3': Fact.FALSE,
    }
})

# add supervisory targets
model.add_labels({
    AB: {
        '0': Fact.TRUE,
        '1': Fact.FALSE,
        '2': Fact.TRUE,
        '3': Fact.FALSE,
    }
})

# train the model and output results
model.infer()
# model.train(losses=Loss.SUPERVISED) # error in example
model.print(params=True)
