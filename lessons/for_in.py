"""An example of for in syntax."""

names: list[str] = ["Bella", "Nole", "Kris", "Bitch"]

# Example 
i: int = 0
while i < len(names): 
    name: str = names[i] 
    print(name)
    i += 1

print("for...input")
# Example 
for name in names: 
    print(name)