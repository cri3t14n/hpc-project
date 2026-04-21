import sys
import os
import pandas as pd

csv_path = sys.argv[1]

df = pd.read_csv(csv_path)

parquet_path = os.path.splitext(csv_path)[0] + ".parquet"
df.to_parquet(parquet_path)

csv_size = os.path.getsize(csv_path)
parquet_size = os.path.getsize(parquet_path)

print(csv_size)
print(parquet_size)
print(csv_size - parquet_size)