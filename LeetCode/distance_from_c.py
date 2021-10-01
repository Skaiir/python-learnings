def shortestToChar(s, c):
    c_positions = [pos for pos, char in enumerate(s) if char == c]
    c_switches = [int((c_positions[x] + c_positions[x + 1]) / 2) + 1 for x in range(len(c_positions) - 1)] + [-1]
    index = 0
    out_arr = []   
    for n in range(len(s)):
        if n == c_switches[index]:
            index += 1
        out_arr.append(abs(n - c_positions[index]))
    return out_arr

shortestToChar("loveleetcode", "e")