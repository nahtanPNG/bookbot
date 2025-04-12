def get_num_words(file_contents):
    file_words = file_contents.split()
    return len(file_words)

def get_characters_count(file_contents):
    file_words = file_contents.split()
    characters = {}

    for word in file_words:
        for character in word:
            lowered = character.lower()
            if lowered in characters:
                characters[lowered] += 1
            else:
                characters[lowered] = 1
    return characters

def sort_on(dict):
    return dict["count"]

def sort_dictionary(dictionary):
    sorted_list = []
    for char, count in dictionary.items():
        new_dict = {"char": char, "count": count}
        sorted_list.append(new_dict)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list