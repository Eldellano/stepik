def update_dictionary(d, key, value):
    if key in d:
        d[key].append(value)
    elif (key not in d) and (2*key in d):
        d[2*key].append(value)
    elif 2*key not in d:
        d[2*key] = [value]
        