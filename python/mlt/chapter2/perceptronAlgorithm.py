#This is a python script that demonstrates how the perceptron learning algorithm works -Sir Nacho

'''
Information regarding the perceptron algorithm
----------------------------------------------
    
CREDIT:
------------
(Based on the book, "Machine Learning With PyTorch and Scikit-learn" created by: 
Sebastian Raschka, Yuxi (Hayden) Liu, and Vahid Mirijalili with foreword by:
Dmytro Dzhulgakov and the Pytorch Core Maintainer. 
Please feel free to support the book as they help make understanding machine learning a lot more easier. 
If you are the authors of the book reading this text and wished for it to be removed, 
please contact me at: steven.frausto@nachoweb.tech and I'll removed this section.)

Perceptron:
------------
What is perceptron algorithm?
Before diving deep into what the algorithm is, it's best to learned what is a biological and artificial
neurons.

Back in good ole day of psychology class in high school, a basic biological neurons are interconnected
nerve cells in the brain that is involved in processing and transmitting chemical and electrical
signals. In short, neurons are basically what helps us Humans learn how to think. The structure of
a neuron contains:

- Dendrites
- Cell Nucleus
- Myelin Sheath
- Axon
- Axon Terminals

Now, it was orginally pitched by McCulloch and Pitts that the nerve cell acts as a simple logic gate with
binary outputs, with multiple signals arrive at the dendrites, they are then integrated into the cell body
and, if the accumulated signal exceeds a certain threshold, an output signal is generated and passed on by
the axon.

Based on how the nerve cell worked, Frank Rosenblatt published the first concept of a learning algorithm called
Perceptron learning.

In short, Rosenblatt has proposed an algorithm that would automatically learn the optimal weight coefficents that
would multipled with the input features in order to make the decision of whether a neuron fires a signal or not.

The perceptron algorithm would be considered supervised learning and classification since it requires user input
to predict whether a new data point belongs to one class or another.

What is supervised learning?:
-------------------------------------------------

In short:
- supervised learning: giving a algorithm an input and have it "predict" the data.
- unsupervised learning: letting a algorithm be in an environment without user input, letting the algorithm use 
the environment and surroundings to learn.
- reinforcement learning: Letting a algorithm learns through the concepts of "rewards" and "punishment", basically
training the algorithm like a dog.

Artificial Neuron:
------------------

This theory is what leds to the creation of artificial neurons. A artificial neurons is based on a binary classification,
tasked with sorting data on two classes, 0 and 1. we can define a decision function, o(z), that takes a linear combination
of certain input values being x, a corresponding weight vector (or array) being w, and z being the net input of w and x:
    
z = w(1)x(1) + w(2)x(2) + ... + w(m)x(m)

Now for example, if x is greater than the defined threhold A, we can predict class 1 or else, class 0. In the Perceptron
Algorithm, the decision function which is o(.) is a variant of a unit step function:

o(z) ---> {if (z >= A) then 1 else 0}                               <----(I know it look messy lol -SirNacho)

to simplify for the code implentation, we can modify the setup by moving the threshold A to the left of the equation:
    
z >= A
Z - A >= 0

We could then defined the bias unit as b = -A and make it part of the net input:
    
z = W(1)X(1) + W(2)X(2) + ... + W(m)X(m) + b = W(t)X + b
    
third, becuase we have the bias unit and the redefinition of the net input of z, we could redefine the decision function, o(z),
by writing:
    
o(z) = {if (z >= 0) then 1 else 0}

Summary:
--------

The whole idea of the MCP neuron and Rosenblatt's threshold perceptron model is to mimic how a single neuron works in the brain,
basically, replicating the theory of how biological neurons work in the first place with the binary computation of the neuron being
based on whether it fires or not after reaching a threshold.

End of Information
------------
'''

#import section:
import numpy as np

#class section:
class perceptron:
    '''

    parameters
    -------------
    eta: float                                              <---concepts such as eta and epoch will be used again later on -Sir Nacho
        learning rate (between 0.0 and 1.0)

    n_iter : int
        Pass over the training dataset

    random_state : int
        random number generator seed for the random weight initialization

    Attributes
    -------------
    w_ : 1d-array
        Weights after fitting
    b_ : scalar
        Bias unit after fitting

    errors_ : list
        Number of misclassifications (updates) in each epoch <--- (does "epoch" sounds familiar :), don't worry, it'll be important later)

    '''

    def __init__(self, eta=0.1, n_iter=50, random_state=1):
        #assigning values to self
        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state

        def fit(self, X, y):
            '''
            Fit the training data.
            
            Parameters
            ----------

            X: {array-like}, shape = [n_examples, n_features]
            Training vectors, where n_examples is the number of examples and n_features is the number of features.
            y: {array-like}, shape = [n_examples]
            Target the values.

            Returns
            -------
            self : object
            '''

            rgen = np.random.RandomState(self.random_state)
            self.w_ = rgen.normal(loc=0.0, scale=0.01, size=X.shape[1])     #weight value
            self.b_ = np.float_(0.)                                         #bias value
            self.error_ = []

            for _ in range (self.n_iter):
                errors = 0
                for xi, target in zip(X, y):
                    update = self.eta * (target - self.predict(xi))
                    self.w_ += update * xi
                    self.b_ += update
                    errors += int(update != 0.0)
                self.errors_.append(errors)
            return self

        def net_input(self, X):
            #calculates the net input
            return np.dot(X, self.w_) + self.b_

        def predict(self,X):
            #returns the class label (0 or 1)
            return np.where(self.net_input(X) >= 0.0, 1, 0)

