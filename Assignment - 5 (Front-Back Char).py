#version 1
def front_back1(word) :
    if len(word) > 1 :
        words = list(word)
        words.insert(0, words.pop(len(words)-1))
        words.insert((len(words)-1), words.pop(1))
        word1 = ""
        return word1.join(words)
    else :
        return word

print(front_back1('clarusway'))
print(front_back1('a'))
print(front_back1('ab'))

print()

#version 2

def front_back2(word) :
    liste = list(word)
    liste[0], liste[(len(word)-1)] = liste[(len(word)-1)], liste[0]
    return "".join(liste)
