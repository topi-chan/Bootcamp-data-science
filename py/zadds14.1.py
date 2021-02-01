
def power(foundation, exponent):
    if foundation == 0: return 0
    return (foundation-1), power(foundation*exponent, exponent)

print(power(3, 3))
