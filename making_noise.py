import pandas as pd
import numpy as np
import random

df = pd.read_csv("online_retail_IIb.csv")


np.random.seed(42)

# 1. Add random missingness
for col in ['Quantity', 'Price']:
    df.loc[df.sample(frac=0.1).index, col] = np.nan

# 2. Convert some numeric values to strings
df.loc[df.sample(frac=0.1).index, 'Quantity'] = df['Quantity'].astype(str)

df.loc[df.sample(frac=0.05).index, 'Price'] = "£" + df['Price'].astype(str)

# 3. Add extreme outliers
df.loc[df.sample(frac=0.01).index, 'Quantity'] = 10000
df.loc[df.sample(frac=0.01).index, 'Price'] = 9999

# 4. Corrupt country names
df.loc[df.sample(frac=0.1).index, 'Country'] = "UK"
df.loc[df.sample(frac=0.05).index, 'Country'] = " united kingdom "

# 5. Corrupt descriptions
df.loc[df.sample(frac=0.05).index, 'Description'] = "###UNKNOWN ITEM@@@"

# 6. Add fake stock codes
df.loc[df.sample(frac=0.02).index, 'StockCode'] = "TEST123"

# 7. Shuffle data
df = df.sample(frac=1).reset_index(drop=True)

df.to_csv("online_retail_noisy_b.csv", index=False)
