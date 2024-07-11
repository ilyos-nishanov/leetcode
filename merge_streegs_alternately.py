def merge_alternately(word1, word2):
    merged_string = ""
    
    # Iterate through the maximum length of the two strings
    for i in range(max(len(word1), len(word2))):
        # Add the character from word1 at the current index (if it exists)
        if i < len(word1):
            merged_string += word1[i]
        
        # Add the character from word2 at the current index (if it exists)
        if i < len(word2):
            merged_string += word2[i]
    
    return merged_string

print(merge_alternately("abc", "xyz"))  # Output: "axbyc"
print(merge_alternately("ab", "xy"))  # Output: "axby"
print(merge_alternately("abcd", "xy"))  # Output: "axbycd"