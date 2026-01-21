#Words longer than 5 characters with alternate capitalization
def long_words_alternate_case(s):
    result = []
    for word in s.split():
        if len(word) > 5:
            new_word = ""
            for i, ch in enumerate(word):
                if i % 2 == 0:
                    new_word += ch.upper()
                else:
                    new_word += ch.lower()
            result.append(new_word)
    return result



# ASCII shifting output
#def shift_string(s):
#    return ''.join(chr((ord(char) - 97 + 1) % 26 + 97) for char in s)
#print(shift_string('hello world')) 
#= ifmmp!xpsme




