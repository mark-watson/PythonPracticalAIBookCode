from lnn import *

model = Model()

# add supervisory targets
model.add_labels({ # example error: add_labels is not defined
    'Smokes': {
        'Ivan': Fact.TRUE,
        'Nick': Fact.TRUE}
    })

# train the model and output results
model.train(losses=Loss.SUPERVISED)
model.print(params=True)
