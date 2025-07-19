
def word_count(text):
    words = text.split()
    return len(words)

def char_counting(text):
    text = text.lower()
    char_count = {}

    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count


def sort_dict(char_count):
    #conver to a list of tuples first
    sorted_items = list(char_count.items())
    sorted_items.sort(key=lambda x: x[1], reverse=True)

    return sorted_items





