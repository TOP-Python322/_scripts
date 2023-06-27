from decimal import Decimal as dec
from fractions import Fraction as frac


# >>> frac('1/3')
# Fraction(1, 3)
# >>>
# >>> frac(3, 25)
# Fraction(3, 25)
# >>>
# >>> frac('0.1')
# Fraction(1, 10)
# >>>
# >>> frac(dec('0.2'))
# Fraction(1, 5)


# >>> num1 = frac('0.12')
# >>> f'{num1!r}'
# 'Fraction(3, 25)'
# >>> f'{num1!s}'
# '3/25'
# >>>
# >>> num1.numerator
# 3
# >>> num1.denominator
# 25
