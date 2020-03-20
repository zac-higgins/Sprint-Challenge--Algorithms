'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
# test_word = "abcthefthghith"

# --------------- Refactored function

def count_th(word):
    occurrences = 0

    def incrementer(word):
        nonlocal occurrences
        try:
            if word.index('th') >= 0:
                new_word = word.replace('th', '', 1)
                occurrences += 1
                incrementer(new_word)
        except:
            return occurrences
        # return occurrences

    incrementer(word)
    return occurrences


# print(count_th(test_word))

# ------------- Original function

# test_word = "abcthefthghith" # Should return 3
# occurrences = 0
# def count_th(word):
#     global occurrences
#     try:
#         if word.index('th') >= 0:
#             new_word = word.replace('th', '', 1)
#             occurrences += 1
#             count_th(new_word)
#     except:
#         return occurrences
#     return occurrences

# print(count_th(test_word))