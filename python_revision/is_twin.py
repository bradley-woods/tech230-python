# Word Twins Problem

# function to return True or False dependent on if a word is a twin or not
def is_twin(a, b):
    empty_string = ""
    sorted_a = empty_string.join(sorted(a.lower()))
    sorted_b = empty_string.join(sorted(b.lower()))
    if sorted_a == sorted_b:
        return True
    else:
        return False


print(is_twin("Silent", "Listen"))
