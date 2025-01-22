#using lists comprensins accepting lists froom the user
# n=[(numbers:=int(input("enter a numbers "))) for _ in range(4)]
# print(n)
lists_len=int(input("enter the length of lists "))
lists=[(numbers:=int(input("enter a number "))) for _ in range(lists_len)]
from functools import reduce
import math
gcf=reduce(math.gcd,lists)
print(gcf)
lcm=reduce(math.lcm,lists)
print(lcm)