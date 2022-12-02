from lnn import Fact, Model, Predicates, Variables, Implies, Equivalent, World

model: Model = Model()

Smokes, Cancer = Predicates('Smokes', 'Cancer') # unused here
Friends = Predicates('Friends', arity=2)

x, y = Variables('x', 'y')

Smoking_causes_Cancer = Implies(Smokes(x), Cancer(x))

Smokers_befriend_Smokers = Implies(Friends(x, y), Equivalent(Smokes(x), Smokes(y)))

formulae = [
    Smoking_causes_Cancer,
    Smokers_befriend_Smokers
]
model.add_knowledge(*formulae, world=World.AXIOM)

# add data to the model
model.add_data({
    Friends: {
        ('Anna', 'Bob'): Fact.TRUE,
        ('Bob', 'Anna'): Fact.TRUE,
        ('Anna', 'Edward'): Fact.TRUE,
        ('Edward', 'Anna'): Fact.TRUE,
        ('Anna', 'Frank'): Fact.TRUE,
        ('Frank', 'Anna'): Fact.TRUE,
        ('Bob', 'Chris'): Fact.TRUE},
    Smokes.name: {
        'Anna': Fact.TRUE,
        'Edward': Fact.TRUE,
        'Frank': Fact.TRUE,
        'Gary': Fact.TRUE},
    Cancer.name: {
        'Anna': Fact.TRUE,
        'Edward': Fact.TRUE}
    })
model.print()
