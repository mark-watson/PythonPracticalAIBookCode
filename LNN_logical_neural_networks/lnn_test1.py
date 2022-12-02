from lnn import *

# define the predicates
x, y = Variables("x", "y")
Smokes, Asthma, Cough = Predicates("Smokes", "Asthma", "Cough")
Friends = Predicate("Friends", arity=2)

# define the connectives/quantifiers
Smokers_have_friends = And(Smokes(x), Friends(x, y))
Asthmatic_smokers_cough = (
    Exists(x, Implies(And(Smokes(x), Asthma(x)), Cough(x))))
Smokers_befriend_smokers = (
    ForAll(x, y, Implies(Smokers_have_friends(x, y), Smokes(y))))

# add root formulae to model
model = Model()
model.add_knowledge(
    Asthmatic_smokers_cough,
    Smokers_befriend_smokers)

# add data to the model
model.add_data({
    Smokes: {
        "Person_1": Fact.TRUE,
        "Person_2": Fact.UNKNOWN,
        "Person_3": Fact.UNKNOWN},
    Friends: {
        ("Person_1", "Person_2"): Fact.TRUE,
        ("Person_2", "Person_3"): Fact.UNKNOWN}})

# reason over the model
model.infer()
#model.train(losses=Loss.SUPERVISED) # errors - mistake in their example

# verify the model outputs
model.print()

