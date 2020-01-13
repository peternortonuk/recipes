

def tuple_slice(start, end, t):
    slice = t[start: end]

    result1 = ','.join(map(str, slice))
    result2 = ','.join([str(i) for i in slice])

    return result1


assert tuple_slice(1, 4, (76, 34, 13, 64, 12)) == '34,13,64'
