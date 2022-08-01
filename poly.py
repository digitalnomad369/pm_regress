#=====  CAPSTONE PROJECT II ======
#====== MACHINE LEARNING: POLYNOMIAL REGRESSION ======

'''This project will use Polynomial regression to discover the relationship
   between different degrees of polynomial regressor using accuracy,
   variance and bias in the relationship between a CEO's years of experience
   and average monthly salary. '''

# ===== LIBRARIES =====
# Import required packages 

import numpy as np
import matplotlib.pyplot as plot
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# ===== SETS =====
# Training set
X_train = [[2], [4], [6], [10], [14]] # years of experience
y_train = [[40000], [60000], [100000], [145000], [150000]] # av monthly salary 
# Testing set
X_test = [[2], [4], [7], [12]] # years of experience
y_test = [[50000], [90000], [120000], [150000]] # av monthly salary

# ===== SUBPLOTS =====
# Create subplots 
figure,axis = plot.subplots(1,2,figsize=(20, 8))
# Train the Linear Regression model and plot a prediction
regressor = LinearRegression()
regressor.fit(X_train, y_train)
xx = np.linspace(0, 22, 100)
yy = regressor.predict(xx.reshape(xx.shape[0],1))
axis[0].plot(xx, yy)

# ===== POLYNOMIAL DEGREES =====
# Establish relation of different degrees used to create Polynomial degrees
# Create Train and Test accuracy lists used to store accuracy of training
# and testing data on different Polynomial models
train_acc_list=[]
test_acc_list=[]
for degree in range(2,8,2):
    # Set the degree of the Polynomial Regression model
    pm_featurizer = PolynomialFeatures(degree=degree)

    # Preprocessor to transform input data matrix
    # into new data matrix of provided degrees
    X_train_poly = pm_featurizer.fit_transform(X_train)
    X_test_poly = pm_featurizer.transform(X_test)

    # Train and test the regressor_quadratic model
    poly_regress = LinearRegression()
    poly_regress = poly_regress.fit(X_train_poly, y_train)
    xx_poly = pm_featurizer.transform(xx.reshape(xx.shape[0],1))

    # Calculate accuracy for training and testing data and store into list
    train_scores=poly_regress.score(X_train_poly,y_train)
    train_acc_list.append(train_scores)
    test_scores=poly_regress.score(X_test_poly,y_test)
    test_acc_list.append(test_scores)
    
    # Plot the graph
    axis[0].plot(xx, poly_regress.predict(xx_poly), linestyle='--',
                 label='Model on degree: {}'.format(degree))
    
# ===== LABELLING OF GRAPH =====
# add legend to graph 
axis[0].legend()
axis[0].set_title("CEO's average monthly salary regressed on years of experience")
axis[0].set_xlabel('Years of experience')
axis[0].set_ylabel('Average monthly salary in Rands')
axis[0].axis([0, 20, 0, 200000])
axis[0].grid(True)
# Create scatterplot for plotting training data
axis[0].scatter(X_train, y_train)

# ===== PLOT TRAINING AND TESTING ACCURACY =====
# Plot training and testing accuracy
# label graph
axis[1].plot(range(2,8,2),train_acc_list,label='Training Accuracy')
axis[1].plot(range(2,8,2),test_acc_list,label='Testing Accuracy')
axis[1].set_xlabel('Polynomial Degree')
axis[1].set_ylabel('Accuracy')
axis[1].set_title('Training and testing set accuracy w.r.t polynomial model degrees')
axis[1].legend()
axis[1].grid(True)

# ===== SAVE AND DISPLAY FIGURES =====
plot.savefig('polynomial_regression.jpg')
plot.show()

'''Conclusions:

Fig A: One can see, as the polynomial degree increases,
       the model overfitted the training set.

Fig B: It is clear that as the polynomial degree increased, the training
set accuracy increased, however, the testing set accuracy decreased
which caused an increase in variance and bias in the model due to
overfitting.

Therefore, we can see that degree = 2 polynomial regressor worked on
the dataset to increase the model's generalization on data compared to other
polynomial degrees used. '''
