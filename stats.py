def get_num_words(in_contents):
    # Here we are removing the spaces from start and end,
    # and breaking every word whenever we encounter a space
    # and storing them in a list. The len of the list is the
    # total count of words.
    return (len(in_contents.strip().split()))


def character_count(in_contents):
    #Here we lowercase the entire string. Then we loop through
    #the dictionary and add each unique character with the
    #current count that each unique character has been encountered
    freq = {}

    for char in in_contents.lower():
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    return freq


def sorted_dictionary_list(in_contents):
    #Reverse sort dictionary by values
    sorted_dict_list = {}
    
    #Sort By Key & Sort By Value
    #sorted_dict_list = dict(sorted(in_contents.items()))
    sorted_dict_list = dict(sorted(in_contents.items(), reverse=True, key=lambda item: item[1]))

    return sorted_dict_list