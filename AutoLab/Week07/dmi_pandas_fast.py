import sys
import pandas as pd

df = pd.read_csv(sys.argv[1])
print(df.loc[df["parameterId"] == "precip_past10min", "value"].sum())