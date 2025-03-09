'''
Homework17
Name: Jai Outland
github link: https://github.com/jaioutland/PYTHON/edit/main/homework17.py
'''

def frequency_counter(lst):
    # Counts the frequency of each element in the list
    freq_dict = {} # Stores frequency 
    for num in lst:
        freq_dict[num] = freq_dict.get(num, 0) + 1
    return freq_dict

nato_alphabet = { 
     'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo',
     'F': 'Foxtrot', 'G': 'Golf','H': 'Hotel', 'I': 'India','J':'Juliett',
     'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November','O':'Oscar', 
     'P':'Papa','Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
     'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray', 'Y': 'Yankee',
     'Z': 'Zulu'} 

def translation(english_words):
    # Translates english words into NATO phonetic alphabet
    for letter in english_words.upper():
        print(nato_alphabet.get(letter, letter))

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest17.py'))