# Import library 
import pandas as pd

df = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/a849660e-ddfa-4033-80a6-94a1b7772e23/update/ds_salaries_statistics', index_col = 0)

# Calculate the variance
var = df["salary"].var()
# Calculate the standard deviation 
std = df["salary"].std()

print('The variace is', round(var, 2))
print('The standard deviation is', round(std, 2))