file_path = (
    r"C:\Users\ronin\Documents\Codes\python_teaching\day_11\file_handling\person.txt"
)

with open(file_path, "w", encoding="utf-8") as f_obj:
    f_obj.write("hello\n")
