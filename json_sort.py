import json
from pandas.io.json import json_normalize

def sort_by_price_ascending(input):
    data = json.loads(input)
    df = json_normalize(data)
    df.sort_values(by=['price', 'name'], inplace=True)
    j = df.to_json(orient='records')
    return j

input = '[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04}]'
expected_output =  '[{"name":"eggs","price":1},{"name":"rice","price":4.04},{"name":"coffee","price":9.99}]'
assert sort_by_price_ascending(input) == expected_output
