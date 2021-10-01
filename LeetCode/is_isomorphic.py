def isIsomorphic(s: str, t: str) -> bool:
    char_map = {}
    t_set = set()
    for x in range(len(s)):
        s_char = s[x]
        t_char = t[x]
        if s_char in char_map:
            if t_char != char_map[s_char]:
                return False
        if t_char in t_set:
            return False
        char_map[s_char] = t_char
        t_set.add(t_char)
    return True   

isIsomorphic("egg", "add")