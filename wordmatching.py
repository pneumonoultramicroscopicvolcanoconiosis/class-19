def word(words):
    count = 0
    lst = []
    for word in words:
        if len(word) > 2 and word[0] == word[-1]:
            count = + 1
            lst.append(word)
    print(lst)
    return count
count = word(["banana", "apple", "shushs"])
print(count)