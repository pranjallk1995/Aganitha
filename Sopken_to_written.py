directory = '/path/to/the/directory'

rep1 = {
	"zero" : "0"
	"one" : "1",
	"two" : "2",
	"three": "3",
	.
	.
	.
	"nine" : "9"
}

rep2 = {
	"dollar" : "$",
	"percent" : "%",
	.
	.
	.
	"and" : "&"
}

def replace_numbers(line):
	for i, j in rep1.iteritems():
		line = line.replace(i, j)
	return line

def replace_symbols(line):
	for i, j in rep2.iteritems():
		line = line.replace(i, j)
	return line

def replace_calls(line):
	words = line.split()
	my_words = ""
	flag = 0
	for word in words:
		if word == "double":
			flag = 1
			continue
		if word == "triple":
			flag = 2
			continue
		if flag == 0:
			my_words += word
		else:
			while flag > 0:
				my_words += word
				flag -= 1
	return my_words

for filename in os.listdir(directory):
	if filename.endswith(".txt"):
		f = open(filename, 'r')
		text = f.read()
		for line in text:
			line = line.lower()
			line = replace_numbers(line)
			line = replace_symbols(line)
			line = replace_calls(line)
		    with open(filename, 'w') as out:
				out.writelines(line)