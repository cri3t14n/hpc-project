import time
import zipfile
import pandas as pd
import pyarrow.csv as csv

def pyarrow_load(path):
    with zipfile.ZipFile(path) as zf:
        name = zf.namelist()[0]
        with zf.open(name) as f:
            table = csv.read_csv(f)
    return table.to_pandas()

path = "/dtu/projects/02613_2025/data/dmi/2023_01.csv.zip"

t0 = time.perf_counter()
df = pd.read_csv(path)
pandas_time = time.perf_counter() - t0

t0 = time.perf_counter()
table = pyarrow_load(path)
pyarrow_time = time.perf_counter() - t0

print("pandas_time:", pandas_time)
print("pyarrow_time:", pyarrow_time)
print("speedup:", pandas_time / pyarrow_time)