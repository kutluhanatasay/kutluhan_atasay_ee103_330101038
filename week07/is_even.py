def is_even_or_odd (n):
    if (n % 2) == 0:
        return "Even"
    if (n % 2) == 1:
        return "Odd"

is_even_or_odd_alias = is_even_or_odd

print(is_even_or_odd)
print(is_even_or_odd_alias)


print(is_even_or_odd(4))
print(is_even_or_odd_alias(4))

print(is_even_or_odd(4) == is_even_or_odd_alias(4))
