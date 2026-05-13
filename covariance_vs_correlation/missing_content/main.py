import pandas as pd 
import numpy as np

df = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/a849660e-ddfa-4033-80a6-94a1b7772e23/update/Stores.csv')

# Calculate the covariance
cov = np.cov(df['Daily_Customer_Count'], df['Items_Available'])[0,1]
# Calculate the correlation
corr = np.corrcoef(df["Daily_Customer_Count"], df["Items_Available"])[0,1]

print("The covariance is", round(cov, 2))
  
print("The correlation is", round(corr, 2))