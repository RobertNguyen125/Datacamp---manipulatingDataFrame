import pandas as pd
users = pd.read_csv('/Users/apple/desktop/manipulatingDataFrames/dataset/users.csv', index_col=0)

users_idx = users.set_index(['city','weekday'])
print(users_idx)

# obtain kv pair by melting users_idx
kv_pairs = pd.melt(users_idx, col_level=0)
print(kv_pairs)
