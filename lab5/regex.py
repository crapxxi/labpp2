import re

txt = "o_odreams breathe life into men, and can cage them in suffering. Men life and die by their dreams, but long after they've been abbandoned, they still smolder deep in men's hearts. Some see nothing more than life and death. They are dead. "
str1_match = re.findall(r'ab*',txt)

if str1_match:
    print(str1_match)

str2_match = re.findall(r'ab{2,3}',txt)
if str2_match:
    print(str2_match)

str3_match = re.findall(r'^[a-z]+_[a-z]+',txt)
if str3_match:
    print(str3_match)

str4_match = re.findall(r'[A-Z][a-z]+',txt)
if str4_match:
    print(str4_match)
    
l = "akakfdakb"
str5_match = re.findall(r'a*b$',l)
if str5_match:
    print(str5_match)


print(re.sub("[ ,.]",":",txt))

text = "snake_case"
print(re.sub(r'_(.)', lambda match: match.group(1).upper(), text))

t = "MathIsSucks"
print(re.findall(r'[A-Z][^A-Z]*',t))

r = "OmaeWaMouSindeYo"
print(re.sub(r'([a-z])([A-Z])', r'\1 \2', r))

s = "camelCaseYo"
print(re.sub(r'([a-z])([A-Z])', r'\1_\2', s).lower())