from collections import deque

def ismatched(expr):
    lefty = "({[" 
    righty = ")}]"
    S = deque()
    for c in expr:
        if c in lefty:
            S.append(c) # push left delimiter on stack
        elif c in righty:
            if len(S)==0:
                return False # nothing to match with
            if righty.index(c) != lefty.index(S.pop()):
                return False 
    return len(S)==0

print(ismatched("( )"))
print(ismatched("((( )(( )){([( )])}))"))
print(ismatched(")(( )){([( )])}"))
print(ismatched("({[ ])}"))
print(ismatched("("))


