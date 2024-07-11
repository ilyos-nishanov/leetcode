def reverseWords(s):
    words = s.split()
    
    # Two-pointer approach to reverse the vowels
    left, right = 0, len(words) - 1
    while left < right:
        words[left], words[right] = words[right], words[left]
        
        #take a step
        left += 1
        right -= 1
    
    return ' '.join(words)

s = "   hello   world "
reversed_s = reverseWords(s)
print(reversed_s)
