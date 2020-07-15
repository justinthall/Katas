sanction_list = ('Peyton North', 'Alanna Hobbs', 'Ayse Sellers', 'Tobey Khan')
test_name1 = 'Peyton North'
test_name2 = 'Alanne Hob'


def test_string_against_stringlist(string, stringlist):
    """This function compares a string to a list of strings, and searches for matches in characters. If a string in the list
    matches 75%, it returns as a hit. The function then returns all hits in a list."""
    hits = []
    for name in stringlist:
        a = 0
        for f in range(len(name)):
            try:
                if string[f] == name[f]:
                    a += 1
            except(IndexError):
                break
        if a / len(name) >= .75:
            hits.append(name)
    return hits


