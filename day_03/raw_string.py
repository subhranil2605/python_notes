# escape character `\`
# special characters: \n, \t,

# my_name = "Subhranil\nSarkar"  # literal string
# print(my_name)

# x = "The new line character in python is: \\n"
x = r"The new line character in python is: \n \n \n \n \n \n" # raw string
print(x)

# use cases
file_path = r"C:\Users\ronin\Documents\Codes\python_teaching\name.txt"
# file_path = "C:\\Users\\ronin\\Documents\\Codes\\python_teaching\\name.txt"

print(file_path)