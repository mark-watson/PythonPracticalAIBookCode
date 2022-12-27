import pandas

def load_data():

    train_df = pandas.read_csv("labeled_cancer_data.csv")
    test_df = pandas.read_csv("labeled_test_data.csv")

    train = train_df.values
    X_train = train[:,0:9].astype(float) # 9 inputs
    print("Number training examples:", len(X_train))
    Y_train = train[:,-1].astype(float)  # one target output (0 for no cancer, 1 for malignant)
    test = test_df.values
    X_test = test[:,0:9].astype(float)
    Y_test = test[:,-1].astype(float)
    print("Number testing examples:", len(X_test))
    return (X_train, Y_train, X_test, Y_test)

