from inspect import stack


# def isValid(s: str) -> bool:
#     o_par = ["{", "[", "(" ]
#     c_par = ["}", "]",  ")"]
#     stack = []
#     for i in range(len(s)):
#         if s[i] in o_par:
#             stack.append(s[i])
#         else:
#             if len(stack) == 0:
#                 return False
#             o = stack.pop()
#             if s[i] != c_par[o_par.index(o)]:
#                 return False
#     return len(stack) == 0

# print(isValid(']'))

def isValid(s: str) -> bool:
    comps = { ")": "(", "]": "[", "}": "{" }
    stack = []
    for ch in s:
        if ch=="(" or ch=="[" or ch=="{":
            stack.append(ch)
        elif ch==")" or ch=="]" or ch=="}":
            if not stack:
                return False
            comp = stack.pop()
            if comps[ch] != comp:
                return False 
    return not stack

print(isValid(']'))



def isValid2(s: str) -> bool:
    stack = []
    m = dict(zip('([{', ')]}'))
    for s2 in s:
        if s2 in "([{":
            stack.append(s2)
        elif not stack or m[stack.pop()] != s2:
            return False
        
    return not stack