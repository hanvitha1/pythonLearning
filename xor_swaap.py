a = 99
b = 3
a = a^b
b = a^b #here b=(a^b)^b | = a^(b^b) (since b^b) | = a^0  = a . so now b became a
a = a^b #here a=(a^b)^a (since b became a in the previous step)| = (a^a)^b | 0^b = b
#both the values of a and be are swapped.
print(f"a is {a}")
print(f"b is {b}")