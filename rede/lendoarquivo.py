# coding: utf-8



with open("teste2.txt") as f:
	file = f.read()
	# for line in f.readlines():
		# a = line.split("\t")
		# print a
		# print line
# print(file)

with open("relatorio.txt", "w") as w:
	w.write(file)