import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

data = pd.DataFrame({'whoAmI': lst})
data = pd.get_dummies(data, columns=['whoAmI'])
# data['tmp'] = True
# data.set_index([data.index, 'whoAmI'], inplace=True)
# data = data.unstack(level=-1, fill_value=False)
# data.columns = data.columns.droplevel()
# data.columns.name = None
print(data)
