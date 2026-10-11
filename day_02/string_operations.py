# String concatenation

first_name = "Rutuja"
last_name = "Deshmukh"

full_name = first_name + " " + last_name
print(full_name)

# String repetition / replication
print("Sorry " * 4)

# String methods

# isnumeric
print("abc".isnumeric())
print("45".isnumeric())
print("45".isnumeric())

# cleaning the string

# .rstrip(), .lstrip(), .strip()
raw_string = "    subhranil"
print(raw_string)
print(raw_string.lstrip())

raw_string = "subhranil                 "
print(f"my name is: {raw_string}.")
print(f"my name is: {raw_string.rstrip()}.")

raw_string = "            subhranil                 "
print(f"my name is: {raw_string}.")
print(f"my name is: {raw_string.strip()}.")

print(len("abc"))
print("abc".__add__(" xzy"))


# Multiline string / Docstring
my_string = "abc"
my_string = "abc"
prompt = """I mostly build AI systems, backend services, and automation platforms in Python.
I have interest in Rust, TypeScript, Nextjs projects.
I'm particularly interested in agentic AI, LLMOps, RAG systems, workflow orchestration, and the infrastructure that makes AI applications reliable in production.
I enjoy working on practical systems that combine reasoning models with APIs, databases, queues, and cloud services rather than purely research-focused machine learning. I tend to prefer lightweight, composable tools and architectures over large monolithic frameworks, and I like understanding how systems work under the hood. While I have full-stack experience, I spend most of my time on backend architecture, AI orchestration, model evaluation, and developer tooling rather than frontend-heavy development.
"""


# prompt = (
#     "I love python programming\n"
#     "I love rust programming"
# )
print(prompt)


# everything is a object

# what is in built function and methods
# len(), max(), min() # it works standalone (functions)
# "sa".count() # methods work on the values

# ------------------------------

# Variable naming conventions

# 1. Skip the reserved keywords in python (like: int, dict, bool, list)
# 2. Can't start the variable name with a number
# 3. Use snake_case formatting mostly for the variable, only use all capital for constant variables
# 4. Can't use space character and special characters inside a variable name (`my variable`, `my&variable`)

# snake case format
my_variable = ""

# constant variable
LEARNING_RATE = 0.3

# private variable
_my_variable = 4


# -----

# escape character -> "\"

print('Rutuja is learning "python"')
print("""Rutuja is learning "python" and 'vscode'.""")

print("Rutuja is learning \"python\" and 'vscode'.")

print("The character to create a new line in python is \\n. This is very useful.")

# ---
# use case of escape character
text_file_path = (
    "C:\\Users\\ronin\\Documents\\Codes\\python_teaching\\day_02\\hello.txt"
)
print(text_file_path)
