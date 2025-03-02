# import math
# t = input()
# numbers = [int(i) for i in t.split(' ')]
# print(math.prod(numbers))
# s = input()
# upper = sum(map(str.isupper, s))
# lower = sum(map(str.islower, s))
# print(f"Upper: {upper} Lower: {lower}")
# word = input()
# if word == "".join(reversed(word)):
#     print(True)
# else:
#     print(False)
# import decimal
# import time
# precision = 5
# decimal.getcontext().prec = precision
# dec = int(input())
# number = decimal.Decimal(dec)
# start_time = time.time()
# time_limit = int(input())/1000
# while True:
#     decimal.getcontext().prec = precision
#     sqrt_result = number.sqrt()
        
#     elapsed_time = time.time() - start_time
#     if elapsed_time >= time_limit:
#         break
#     precision += 5 
# print(f"Result: {sqrt_result} elapsed time: {elapsed_time}")
# tupl = (True, False, True)
# print(all(tupl))
