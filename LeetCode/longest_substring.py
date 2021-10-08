def lengthOfLongestSubstring(s: str) -> int:
    max_len = 0
    invalid_range = 0
    for i in range(len(s)):
        if invalid_range > 0:
            invalid_range -= 1
        if not s[i] in s[i - max_len: i]:
            if invalid_range == 0:
                max_len += 1
        else:
            invalid_range = max(s[i - max_len: i].rfind(s[i]) + 1, invalid_range)
    return max_len

lengthOfLongestSubstring("ruowzgiooobpple")