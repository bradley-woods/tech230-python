# Sort Sentence By Word Length Problem

# function returns list of words in ascending order by length of word
def sort_by_length_of_words(string):
    sorted_words = string.split()
    sorted_words.sort(key=len)
    return sorted_words


print(sort_by_length_of_words("here is a block of text with differing sized words"))
