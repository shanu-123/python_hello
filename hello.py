print("Hello World")

with open("data.txt","w") as fd:
	data = "shanu"
	for i in data:
		fd.write(i)

