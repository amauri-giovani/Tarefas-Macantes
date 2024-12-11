import re


print(re.compile('Eduard'))

a = re.search('a', 'eduardo')
print(a.end())
print(a.start())
print(a.span())


b = re.split(r'.ar', 'eduardo')
print(b)

c = re.findall('a', 'aaaaaaa')
print(c)

d = re.findall('ae', 'aaaaaae')
print(d)

e = re.findall('.a', 'aaaaaae')
print(e)

f = re.search('.', 'Python')
print(f)

