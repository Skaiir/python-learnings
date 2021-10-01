def isPalindrome(s):
    alnum_s = "".join(c for c in s if c.isalnum()).lower()
    return alnum_s == str(alnum_s[::-1]) 

isPalindrome("A man, a plan, a canal: Panama")