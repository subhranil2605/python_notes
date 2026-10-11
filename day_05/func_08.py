# default values

# def generate_answer(query, model, temp=0.9, top_k=4):
#     model = openai(model=model, temperature=temp, topK=top_k)

#     return model.invoke(query)

# generate_answer(
#     query="Who is the better python programmer? rutuja or subhranil",
#     model="gpt-4o-mini",
#     temp=0.3,
#     top_k=4,
# )


def calculate(name, age, y, x=5):
    print(f"hello, {name}")
    print(f"Age {age}")
    result = x * y
    print(result)


calculate("Subhranil", 27, 5, 6)
calculate("Subhranil", 27, 4)
calculate("Rutuja", 26, 8)
