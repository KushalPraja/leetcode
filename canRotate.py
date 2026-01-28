def can_rotate(s, goal):
    s = [i for i in s]

    for i in range(len(s)):
        last_string = s[-1]
        for i in range(len(s) - 1, 0, -1):
            s[i] = s[i-1]
        s[0] = last_string
        if "".join(s) == goal:
            return True

    return False


print(can_rotate("hello", "oheil"))
       
