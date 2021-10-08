def countAndSay(n: int) -> str:
    count_and_say = "1" 
    for _ in range(n - 1):
        next_count_and_say = []
        working_char = count_and_say[0]
        count = 1
        for char in count_and_say[1:]:
            if char != working_char:
                next_count_and_say.append(str(count))
                next_count_and_say.append(working_char)
                working_char = char
                count = 1
            else:
                count += 1
        next_count_and_say.append(str(count))
        next_count_and_say.append(working_char)
        count_and_say = "".join(next_count_and_say)
    return count_and_say

countAndSay(4)