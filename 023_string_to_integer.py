def string_to_integer(s):
    if not s:
        return "Invalid input"

    result = 0
    start_index = 0

    for i in range(start_index, len(s)):
        char = s[i]
        if '0' <= char <= '9':
            digit = ord(char) - ord('0')
            result = result * 10 + digit
    print(result)
    return result

string_to_integer("123")