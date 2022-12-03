# Reverse Digits -312 -> -213

def reverse_int(x: int):
    result, x_left = 0, abs(x)
    while(x_left):
        result = result * 10 + x_left % 10
        x_left //= 10
    return -result if x < 0 else result

# print(reverse_int(900))
# print(reverse_int(-3214))
# print(reverse_int(7878878))

