# Import library
import pandas as pd

df = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/a849660e-ddfa-4033-80a6-94a1b7772e23/update/ds_salaries_statistics', index_col = 0)

# Calculating the mean value
mean = df["salary"].mean()
# Calculating the median value
median = df["salary"].median()

print('The mean value is', mean)
print('The median value is', median)