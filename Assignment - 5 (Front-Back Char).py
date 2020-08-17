def front_back(word) :
    if len(word) > 1 :
        words = list(word)
        words.insert(0, words.pop(len(words)-1))
        words.insert((len(words)-1), words.pop(1))
        word1 = ""
        return word1.join(words)
    else :
        return word

print(front_back('clarusway'))
print(front_back('a'))
print(front_back('ab'))
