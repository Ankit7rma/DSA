def is_unique2(  s)  :
     
    if s is None or len(s) > 26:
        return False
    
    checker = 0
    for char in s:
        val = ord(char) - ord('a')
        if (checker & (1 << val)) > 0:
            return False
        checker |= (1 << val)
    
    return True

s = "abcb"
iu = is_unique2(s)
print(iu)
  