a = ["Alice", "Bob", "Charlie", "David", "Eva"]
b = ["Charlie", "David", "Frank", "Grace", "Helen"]


com = list(set(a)^set(b))
print(com)  # Output: ['Alice', 'Bob', 'Eva', 'Frank', 'Grace', 'Helen']