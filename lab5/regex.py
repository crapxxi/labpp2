import re

txt = "o_odreams breathe life into men, and can cage them in suffering. Men life and die by their dreams, but long after they've been abbandoned, they still smolder deep in men's hearts. Some see nothing more than life and death. They are dead. "
str1_match = re.findall(r'ab*',txt)
# if str1_match:
#     print(str1_match)
str2_match = re.findall(r'ab{2,3}',txt)
# if str2_match:
#     print(str2_match)
str3_match = re.findall(r'^[a-z]+_[a-z]+',txt)
# if str3_match:
#     print(str3_match)
str4_match = re.findall(r'[A-Z][a-z]+',txt)
# if str4_match:
#     print(str4_match)
l = "akakfdakb"
text = "snake_case"
t = "MathIsSucks"
str5_match = re.findall(r'a*b$',l)
# if str5_match:
#     print(str5_match)
# str6_match = re.sub("[ ,.]",":",txt)
# print(str6_match)
res = text.split('_')
camel = res[0] + ''.join(word.capitalize() for word in res[1:])
# print(camel)
str8_match = re.findall(r'[A-Z][^A-Z]*',t)
# print(str8_match)
r = "OmaeWaMouSindeyo"
res1 = ' '.join(re.findall(r'[A-Z][^A-Z]*',r))
# print(res1)
s = "camelCaseYo"
print(re.sub(r'([a-z])([A-Z])', r'\1_\2', s).lower())