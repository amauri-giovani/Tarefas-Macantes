import re

text = 'Pig latin is cool!'
reg = re.sub(r'(\w{1})(\w*)', r'\2\1ay', text)


print(reg)