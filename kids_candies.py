def kids_candies (candies:list, extra:int):
    result = []
    for i in candies:
        if i+extra < max(candies):
            result.append(False)
        else:
            result.append(True)

    return result

print(kids_candies([2,3,5,1,3], 3))
print(kids_candies([4,2,1,1,2], 1))
print(kids_candies([12,1,12], 10))