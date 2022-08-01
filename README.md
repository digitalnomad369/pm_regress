# pm_regress

# TABLE OF CONTENTS #

[System Objectives and Description](#System-Objectives-and-Description)

[System Requirements and Installation](#System-Requirements-and-Installation)

[Application components](#Application-components)

[Sample output](#Sample-output)

[Contributors](#Contributors)

[License and Copyright](#License-and-Copyright)

# System Objectives and Description

The pm_regress project will use Polynomial regression to discover the relationship
between different degrees of polynomial regressors using accuracy, variance and bias 
in the relationship between a CEO's years of experience and average monthly salary.

# System Requirements and Installation

As the program is coded in Python, in order to run and test the code, the following IDE is required:

__- The Python IDE:__
To download the Python IDE, click on the following link to access the official Python website: 
*https://www.python.org/downloads/*

Alternatively, you can download Visual Studio Code which also supports compatibility for Python code
- To download the Visual Studio Code IDE including the Coding Pack for Python, click on the following link: 
*https://code.visualstudio.com/docs/python/coding-pack-python*

In order to perform machine learning algorithms, you will also be required to install the Python SciPy, 
NumPy, Matplotlib and Sci-Kit learn packages. 

To install these packages, do the following:

- Open the command prompt or terminal on your device
- To install SciPy, type “__pip install scipy__” and press Enter.
- To install NumPy, type “__pip install numpy__” and press Enter.
- To install Matplotlib, type “__pip install matplotlib__” and press Enter.
- To install Sci-Kit, type “__pip install sklearn__” and press Enter.

# Application components 

To improve the structure and readability of the code, the __poly.py__ file is comprised of the following code blocks:

__Libraries:__: This block imports all required packages (numpy, 
matplotlib, LinearRegression from sklearn.linear_model and PolynomialFeatures from 
sklearn.preprocessing package)

__Sets:__: Declare and initialize the training and testing sets 
(the x-variable is the years of experience and the y-variable is the CEO's av
monthly salary)

__Subplots:__: Create subplots and train the LinearRegression model to 
plot a prediction using the training data. 

__Polynomial Degrees:___ 
- Establish the relation of different degrees to create Polynomial Degrees;
- Create train and accuracy lists to store accuracy of train and test data on different Polynomial models. 
- Plot graph




