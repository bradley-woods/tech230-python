# Password Size Evaluator Problem

# function to evaluate length of password
def password_size(string):
    if len(string) < 5:
        return "Your password is too short"
    elif len(string) > 20:
        return "Your password is too long and may be forgotten"
    else:
        return "Your password is an acceptable length"


print(password_size("abc"))
print(password_size("abcdefghijklmnopqrstuv"))
print(password_size("abcdef"))
