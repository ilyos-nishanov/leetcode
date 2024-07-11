def gcdOfStrings(str1, str2):
    # If the concatenation of the two strings is not equal, then there is no common divisor
    if str1 + str2 != str2 + str1:
        return ""
    
    # Find the gcd of the lengths of the two strings
    gcd = lambda a, b: a if b == 0 else gcd(b, a % b)
    length = gcd(len(str1), len(str2))
    
    # The largest string x that divides both str1 and str2 is the substring of str1 of length 'length'
    return str1[:length]

print(gcdOfStrings("ABCABC", "ABC"))  # Output: "ABC"
print(gcdOfStrings("abc", "abcabc"))  # Output: "ABC"
print(gcdOfStrings("ABABAB", "ABAB"))  # Output: "AB"
print(gcdOfStrings("LEET", "CODE"))  # Output: ""
print(gcdOfStrings('asdfleetcodeasde', 'leetcode'))