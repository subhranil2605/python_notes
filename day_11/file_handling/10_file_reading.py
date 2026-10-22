f_obj = open("person.txt", "r", encoding="utf-8")

data = f_obj.read()
print(data)

f_obj.close()
