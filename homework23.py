'''
Homework23
Name: Jai Outland
github link:
'''


def group_by_first_letter(words):
    result = {}   # Store all words by first letter
    for word in words:
        first_letter = word[0].lower()
        if first_letter not in result:
            result[first_letter] = []
        result[first_letter].append(word)
    return result


def convert_to_sentence(words):
    # Joins words together with a period at the end
    return str(" ".join(words) + ("." if words else ""))


if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest23.py'))
