text = input("Text: ").lower()
words = text.split()
word_quantities = {}
for word in words:
    if word in word_quantities:
        word_quantities[word] += 1
    else:
        word_quantities[word] = 1
list_of_keys = []
for key in word_quantities.keys():
    list_of_keys.append(key)
list_of_keys.sort()
longest_string = max(list_of_keys, key=len)
for word in list_of_keys:
    print("{:{}} : {}".format(word, len(longest_string), word_quantities[word]))
