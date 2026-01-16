import sys
import pandas as pd 

df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})


print("arguments:", sys.argv)

print("hello ", sys.argv[1])

print(df)