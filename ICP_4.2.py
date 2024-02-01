import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Importing the dataset
df = pd.read_csv('Salary_Data.csv')  # Replace with your file path

# Splitting the dataset into the training set and test set
X = df.iloc[:, :-1].values  # Independent variable 'YearsExperience'
y = df.iloc[:, -1].values   # Dependent variable 'Salary'
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3, random_state=0)

# Fitting Simple Linear Regression to the Training set
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

# Calculating the Mean Squared Error
mse = mean_squared_error(y_test, y_pred)

# Visualizing the Training set results
plt.scatter(X_train, y_train, color='blue', label='Training data')
plt.scatter(X_test, y_test, color='red', label='Test data')
plt.plot(X_train, regressor.predict(X_train), color='green')
plt.title('Years of Experience vs Salary (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.legend()
plt.show()

print("Mean Squared Error:", mse)