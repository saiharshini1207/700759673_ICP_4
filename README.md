#code 1


Each column's missing values are checked using the isnull() method, and the number of null values in each column is then counted using the sum() function. The null_values variable contains the results.
The 'Calories' and 'Pulse' columns using various functions (min, max, count, mean) and stores the results in the aggregated_data variable.

This line takes the 'Maxpulse' column out of the df_filled DataFrame and generates a new one called df_modified.

Basic statistical data (count, mean, std, min, 25%, 50%, 75%, max) regarding the numerical columns in the DataFrame df are produced by the describe() method. The description variable contains the results.
