#code 1


Each column's missing values are checked using the isnull() method, and the number of null values in each column is then counted using the sum() function. The null_values variable contains the results.
The 'Calories' and 'Pulse' columns using various functions (min, max, count, mean) and stores the results in the aggregated_data variable.

This line takes the 'Maxpulse' column out of the df_filled DataFrame and generates a new one called df_modified.

Basic statistical data (count, mean, std, min, 25%, 50%, 75%, max) regarding the numerical columns in the DataFrame df are produced by the describe() method. The description variable contains the results.

the absent entries in the DataFrame (df) containing each column's mean value. An entirely new DataFrame called df_filled holds the result.

'Calories' and 'Pulse' columns are used as filters to filter rows, and the result is stored in the filtered_calories_pulse variable.


#code 2

The first step of the code is to import the required libraries: matplotlib.pyplot for plotting, pandas for data manipulation, and the needed scikit-learn modules for machine learning.
Bring in Dataset:


The dataset is loaded using the pandas library's pd.read_csv method from a CSV file called "Salary_Data.csv." The actual path must be used in place of the file path.
Data division:

The years of experience are represented by the independent variable (X) in the dataset, while the wage is represented by the dependent variable (y). Training and testing sets are created using scikit-learn's train_test_split function.
The model of linear regression:

The LinearRegression class from scikit-learn is used to generate a basic linear regression model. The fit method is used to fit the model to the training set.
Forecast:

The model that has been trained is utilized to on the test set are kept in y_pred, along with the anticipated values.
Compute Mean Squared Error:

The mean_squared_error function from scikit-learn is used to determine the mean squared error (MSE). The average squared difference (MSE) between the expected and actual values is a measurement.
Illustration:

To see the training and test data points, the code generates a scatter plot. On top of the plot is the regression line, which represents the training set's projected values.
Print MSE:

The console displays the computed mean squared error.
