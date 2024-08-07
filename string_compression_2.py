def compress(chars: list[str]):
    my_dict = {}
    for char in chars:
        if char in my_dict:
            my_dict[char] += 1
        else:
            my_dict[char] = 1
    
    chars = ''
    for key, value in my_dict.items():
        chars += key
        # if value >1:
        #     for i in list(str(value)):
        chars += str(value)

            
    return (chars)
        
        
    
    


print(compress(["a","a","b","b","c","c","c"]))
print(compress(["a"]))
print(compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))

            
            