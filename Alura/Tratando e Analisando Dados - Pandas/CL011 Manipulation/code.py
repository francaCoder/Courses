import pandas as pd

data = [0.5, None, None, 0.52, 0.54, None, None, 0.59, 0.6, None, 0.7]
s = pd.Series(data)
print(s.fillna(0))

# Methods='ffill' → Take the previous and replace the current (up to down)
# Methods='bfill' → Take the previous and replace the current (down to up)
# mean → average
# limit