import pandas as pd
import numpy as np
import sklearn as sk

housing_data = pd.read_csv("housing.csv")
print(housing_data)
print("############################         INFO")
housing_data.info()
print("############################         DESCRIBE")
print(housing_data.describe())

print("Getting different values of the column 'ocean_proximity'")
print(housing_data["ocean_proximity"].value_counts())


def split_train_test(data, test_ratio):
    #Below lines will remember and give me same randoms everytime the code is executed
    # np.random.seed(len(data))
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_set_indices = shuffled_indices[:test_set_size]
    train_set_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_set_indices], data.iloc[test_set_indices]
    # print(f'test set size: {test_set_size}')
    # print(f'test set indices: {len(test_set_indices)}')
    # print(f'train set indices: {len(train_set_indices)}')


np.random.seed(42)
train_set, test_set = split_train_test(housing_data, 0.2)
