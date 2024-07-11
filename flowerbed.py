
def canPlaceFlowers(flowerbed, n):
    """
    :type flowerbed: List[int]
    :type n: int
    :rtype: bool
    """
    count = 0
    length = len(flowerbed)
    
    for i in range(length):
        if flowerbed[i] == 0:
            prev = 0 if i == 0 else flowerbed[i-1]
            next = 0 if i == length-1 else flowerbed[i+1]
            if prev == 0 and next == 0:
                flowerbed[i] = 1
                count += 1
                if count >= n:
                    return True
    
    return count >= n


print(canPlaceFlowers([0,1,1,0,0,0,1,0,0,1,0,0,0], 2))