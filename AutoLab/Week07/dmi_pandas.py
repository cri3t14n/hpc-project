import pandas as pd

def df_memsize(df):
    return df.memory_usage(deep=True).sum()

df = pd.read_csv("/dtu/projects/02613_2025/data/dmi/2023_01.csv.zip")
print(df_memsize(df))



def reduce_dmi_df(df):
    df = df.copy()

    for col in ["parameterId", "stationId"]:
        if col in df.columns:
            df[col] = df[col].astype("category")

    for col in ["created", "observed"]:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col])

    for col in ["coordsx", "coordsy", "value"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], downcast="float")

    return df


print(reduce_dmi_df(df))