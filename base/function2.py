def exp(base, exp=2.71):
    print(base ** exp)


# >>> exp
# <function exp at 0x000002C7BEC72D40>
# >>>
# >>> exp(3, 2)
# 9
# >>>
# >>> exp(5)
# 78.3806231175926
# >>>
# >>> exp(base=11, exp=2)
# 121
# >>>
# >>> exp(exp=6)
# ...
# TypeError: exp() missing 1 required positional argument: 'base'
# >>>
# >>> exp('2', '5')
# ...
# TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'str'

