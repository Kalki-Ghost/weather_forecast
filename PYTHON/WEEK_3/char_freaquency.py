def char_fre(string):
    frequency = {}
    string = string.upper()
    for i in string:

        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1
    return frequency


String = "Suhas is a good boy"
print(char_fre(String))
