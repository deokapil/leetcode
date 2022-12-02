from itertools import groupby
from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    retval: str = ""
    min_len: int = min([len(x) for x in strs])
    for i in range(min_len):
        all_at_i: List[str] = [x[i] for x in strs]
        g = groupby(all_at_i)
        if next(g, True) and not next(g, False):
            retval += all_at_i[0]
        else:
            break
    return retval
    

print(longestCommonPrefix(["abbcd", "abdev", "abjklop", "abkkr"]))