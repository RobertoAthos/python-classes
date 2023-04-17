import pandas as pd

file_path = "https://pycourse.s3.amazonaws.com/temperature.csv"
df = pd.read_csv(file_path)
print(df)
