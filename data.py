import pandas as pd
import numpy as np


df = pd.DataFrame(np.random.randn(10,5))

print(df)
df.to_json('data.json', orient='records', lines=True)
