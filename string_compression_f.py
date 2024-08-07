# chars = ["a","a","b","b","c","c","c"]
# chars = ["a"]
chars = ["c","a","a","a","a","b","b","a","a","d","e","e"]    


class Solution:
    def compress(self, chars: list[str]) -> int:
        def inner(chars: list):
            if not chars: return ""
            count = 0
            while chars:
                count += 1
                char = chars.pop(0)
                if chars and char != chars[0]: break 
            return char + (str(count) if count-1 else "") + str(inner(chars))
        s = inner(chars)
        chars.extend(s)
        return len(chars)


class Solution:
    def compress(self, chars: list[str]) -> int:
        s = ""
        while chars:
            cnt = 0
            while chars:
                char = chars.pop(0)
                cnt += 1
                if chars and char != chars[0]: break
            s += char + (str(cnt) if cnt-1 else "")
        chars.extend(s)
        return len(chars)



class Solution:
    def compress(self, chars: list[str]) -> int:
        cnt = 0
        old = ""
        s = ""
        chars.append("")
        for char in chars:
            if old != char:
                if cnt and cnt != 1:
                    s += str(cnt)
                cnt = 0
                s += char
                old = char
            cnt += 1 
        del chars[:]
        chars.extend(s)
        return len(s) 


class Solution:
    def compress(self, chars: list[str]) -> int:
        s = ""
        cnt = 0
        chars.append("")
        # chars.reverse()
        while chars and (char := chars.pop(0)):
            cnt += 1
            if chars and char == chars[0]:
                continue
            s += char + (str(cnt) if cnt -1 else "")
            cnt = 0
        chars.extend(s) 
        return len(chars)
