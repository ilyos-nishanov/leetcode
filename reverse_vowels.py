def reverseVowels(s):
    vowels = 'aeiouAEIOU'
    char_list = list(s)
    
    # Two-pointer approach to reverse the vowels
    left, right = 0, len(char_list) - 1
    while left < right:
        while left < right and char_list[left] not in vowels:
            left += 1
        
        while left < right and char_list[right] not in vowels:
            right -= 1
        char_list[left], char_list[right] = char_list[right], char_list[left]
        
        #take a step
        left += 1
        right -= 1
    
    return ''.join(char_list)

s = "hello"
reversed_s = reverseVowels(s)
print(reversed_s)  # Output: "holle"

s = "leetcode"
reversed_s = reverseVowels(s)
print(reversed_s)  # Output: "leotcede"