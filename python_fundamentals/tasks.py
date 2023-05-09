# Task 1
print("Task 1")
a = True
b = False

print(a == b)
print(a != b)
print(a >= True)
print(b <= False)

# Task 2
print("\nTask 2")
hi = "Hello World!"
print(hi.isalpha())
print(hi.islower())
print(hi.endswith("!"))
print(hi.startswith("H"))

# Task 3
print("\nTask 3")
print(bool(0))
print(bool(""))
print(bool(None))

# Task 4
print("\nTask 4")
print("None = NoneType, no value so cannot be checked using ==")

# Task 5
print("\nTask 5")
# Lists = mutable, ordered and indexed
# Tuples = immutable, ordered and indexed
# Dicts = mutable, unordered and indexed (key/value)
# Sets = mutable, unordered and not indexed

list_ = [1, 2, 3]
tuple_ = (1, 2, 3)
dict_ = {"one": 1, "two": 2, "three": 3}
set_ = {1, 2, 3}

list_[0] = 4
dict_["two"] = 6

print(list_[0])
print(tuple_[1])
print(dict_["two"])
