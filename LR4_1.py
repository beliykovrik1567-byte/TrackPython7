# TODO решите задачу
import json
def task() -> float:
    with open('input.json') as json_file:
        input_data  = json.load(json_file)
        sum_of_products = 0
    for item in input_data :
        score = item["score"]
        weight = item["weight"]
        sum_of_products += score * weight
    return round(sum_of_products, 3)
print(task())
