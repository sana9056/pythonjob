def get_dictionary(keys, values):
    values.extend([None] * (len(keys) - len(values)))
    return {key: value for (key, value) in zip(keys, values)}


print(get_dictionary([3, 7, 45, 76], [44, 66]))
