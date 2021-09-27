def canConstruct(ransomNote: str, magazine: str) -> bool:
    mag_p = 0
    mag_dict = {}
    mag_len = len(magazine)
    for char in ransomNote:
        if char in mag_dict and mag_dict[char] > 0:
            mag_dict[char] -= 1
        elif mag_p < mag_len:
            while mag_p < mag_len:
                p_letter = magazine[mag_p]
                mag_p += 1
                if p_letter != char:
                    if mag_p == mag_len:
                        return False
                    mag_dict[p_letter] = mag_dict[p_letter] + 1 if p_letter in mag_dict else 1
                else:
                    break
        else:
            return False
           
    return True

canConstruct("jjhafiecg", "gj")

"jjhafiecg"
"gj"
