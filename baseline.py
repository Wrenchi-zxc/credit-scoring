import pandas as pd

df = pd.read_csv("data/cs-training.csv", index_col=0)

mInc = df["NumberOfDependents"].median()
print(mInc)
