import json
from pandas.io.json import json_normalize

def sort_by_price_ascending1(input):
    # create list of dicts from raw string
    data = json.loads(input)
    # create a pandas dataframe
    df = json_normalize(data)
    # sort the dataframe
    df.sort_values(by=['price', 'name'], inplace=True)
    return df.to_json(orient='records')


def sort_by_price_ascending2(input_str):
    # create list of dicts from raw string
    data = json.loads(input_str)
    # sort the list
    return sorted(data, key=lambda x: (x['price'], x['name']))


input_str = '[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04}]'
expected_output_str = '[{"name":"eggs","price":1},{"name":"rice","price":4.04},{"name":"coffee","price":9.99}]'
expected_output_json = json.loads(expected_output_str)

assert sort_by_price_ascending2(input_str) == expected_output_json
