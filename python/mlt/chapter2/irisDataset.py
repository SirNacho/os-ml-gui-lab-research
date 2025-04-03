#This is a script that uses the iris dataset on the perceptron model. -Sir Nacho

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import perceptronAlgorithm as perceptron


def showLastFiveLines(offline : bool):
    
    '''Shows the last five lines of iris.data using tail()'''
    if (offline == True):
        s = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
        print("From URL:", s)
    else:
        s = "iris.data"
        print("From file:", s)
    df = pd.read_csv(s, header=None, encoding='utf-8')
    print(df.tail())
    y = df.iloc[0:100, 4].values
    y = np.where(y == 'Iris-setosa', 0, 1)
    X = df.iloc[0:100, [0, 2]].values
    plt.scatter(X[:50, 0], X[:50, 1],
                color='red', marker='o', label='Setosa')
    plt.scatter(X[50:100, 0], X[50:100, 1],
                color='blue', marker='s', label='Versicolor')
    plt.xlabel('Sepal length [cm]')
    plt.ylabel('Petal length [cm]')
    plt.legend(loc='upper left')
    plt.show()

    ppn = perceptron.perceptron(eta=0.1, n_iter=10)
    ppn.fit(X, y)
    plt.plot(range(1, len(ppn.errors_) + 1), ppn.errors_, marker='o')
    plt.xlabel("Epochs")
    plt.ylabel("Number of updates")
    plt.show()

if __name__ == "__main__":
    showLastFiveLines(True)
