sanction_list = ('Peyton North', 'Alanna Hobbs', 'Ayse Sellers', 'Tobey Khan')
test_name1 = 'Peyton North'
test_name2 = 'Alanne Hobbs'


def test_payee_against_transaction(payee, sanctions):
    """problem: with a list of sanctioned names, return wether or not a payee is on the list. The function must also
   account for misspellings, and must return when payees reach a 75% match rate.
   Solution: This function runs through the sanctions list, and then runs through each character in each name on the sanctions
   list to the payee's name. If two characters match, the counter a is updated to show the match. if the name meets the
   75% match rate, it is added to a list of all hits, and then returned."""
    hits = []
    for name in sanctions:
        a = 0
        for f in range(len(name)):
            if payee[f] == name[f]:
                a += 1
            else:
                continue
        if a / len(name) >= .75:
            hits.append(name)
    return hits


print(test_payee_against_transaction(test_name2, sanction_list))
