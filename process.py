import os
import pandas as pd

os.makedirs("data",exist_ok=True)
src="data/sensor_log.csv"
dst="data/aggregates.csv"

df=pd.read_csv(src)
df["timestamp"]=pd.to_datetime(df["timestamp"])
df=df.set_index("timestamp").resample("1min").mean(numeric_only=True)
df=df.reset_index().rename(columns={"timestamp":"minute"})
df.to_csv(dst,index=False)
print("wrote",dst)
