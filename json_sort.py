import json
from pandas.io.json import json_normalize

def sort_by_price_ascending1(input):
    data = json.loads(input)
    df = json_normalize(data)
    df.sort_values(by=['price', 'name'], inplace=True)
    j = df.to_json(orient='records')
    return j

def sort_by_price_ascending2(input):
    data = json.loads(input)
    return sorted(data, key=lambda x: (x['price'], x['name']))


input_str = '[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04}]'
expected_output_str = '[{"name":"eggs","price":1},{"name":"rice","price":4.04},{"name":"coffee","price":9.99}]'
expected_output_json = json.loads(expected_output_str)

assert sort_by_price_ascending2(input_str) == expected_output_json
