# Name: Richard Castro
# CSE 160 20au Final Exam - Part 1
# Be sure you also complete Part 2, found in Gradescope!

# Problem 1
def every_set(list_of_sets):
    '''
    list_of_sets: a list of sets of integers
    Returns: a list containing only the integers found in every set
    If no common elements are found, an empty list should be returned.
    There is guaranteed to be at least one set in list_of_sets.
    The order of the integers in the returned list does not matter.
    If list_of_sets contains only one set, then return a list containing
    the values in that set.
    '''
    same = []
    # Only if there is one set in the list
    if len(list_of_sets) == 1:
        return list(list_of_sets[0])
    else:
        for i in range(len(list_of_sets) - 1):
            # duplicates
            same.append(list_of_sets[i] & list_of_sets[i + 1])
            # This happens for a list with more than 2 sets in it
            if i > 0:
                same[0] = same[0] & same[1]
                same.remove(same[1])
    return list(same[0])


def test_every_set():
    assert every_set([{1, 2, 3}]) == [1, 2, 3]
    assert sorted(every_set([{1, 2, 3}, {1, 2}])) == [1, 2]
    assert every_set([{1, 2, 3}, {-5}]) == []
    assert every_set([{1, 2, 3, 8}, {1, 2, 7}, {1, 9}]) == [1]
    assert every_set([set()]) == []


# Problem 2
def get_sorted_veggies(vendor_inventory):
    '''
    vendor_inventory: dict whose keys are strings containing the name of a
                    vendor and whose values are strings listing different
                    vegetables separated by whitespace
    Returns: a list of all of the unique types of vegetables being sold,
            sorted in descending order by number of vendors that sell that
            type of vegetable.
    If there is a tie between the number of vendors,
    the tied vegetables should be listed in alphabetical order.
    Passing in an empty dictionary should return an empty list,
    as should passing in a dictionary whose values are all empty strings.
    Assume the string of vegetables for each vendor does not contain
    duplicates, and that all the vegetable names are in lowercase.
    '''
    num_vendors = dict()
    vegtables = []
    if vendor_inventory == {}:
        return vegtables

    # Creates and fills num_vendors. Keys: Vegtables name Values: # of vendors
    for key in vendor_inventory.keys():
        split_vegtables = vendor_inventory[key].split()
        for veg in split_vegtables:
            if veg not in num_vendors.keys():
                num_vendors.setdefault(veg, 0)
            num_vendors[veg] += 1

    num_of_vendors = sorted(num_vendors.values(), reverse=True)
    alphabetical = dict()
    dont_repeat = int()

    # Creates and fills alphabetical dictionary.
    # Key: # of vendors & Values: list of unique vegtables
    for num in num_of_vendors:
        if dont_repeat != num:
            for key in num_vendors.keys():
                if num_vendors[key] == num:
                    alphabetical.setdefault(num, [])
                    alphabetical[num].append(key)
        dont_repeat = num

    combine = []
    # Sorts alphabetical dictionary by key(int of vendors) by decending order
    # Combines all the sorted lists in dictionary
    for each in sorted(alphabetical.keys(), reverse=True):
        combine += sorted(alphabetical[each])
    return combine


def test_get_sorted_veggies():
    assert get_sorted_veggies({}) == []
    vi1 = {'vendor2': '', 'vendor3': '', 'vendor6': ''}
    assert get_sorted_veggies(vi1) == []
    vi2 = {'vendor1': 'cucumber cauliflower tomatoes',
            'vendor2': 'cucumber cauliflower potatoes'}
        assert get_sorted_veggies(vi2) == ['cauliflower', 'cucumber',
                                        'potatoes', 'tomatoes']
        vi3 = {'vendor2': "", 'vendor3': 'apples'}
        assert get_sorted_veggies(vi3) == ['apples']
        vi4 = {'vendor2': "spinach artichoke carrots",
            'vendor3': 'spinach parsnips celery',
            'vendor5': 'spinach carrots'}
        assert get_sorted_veggies(vi4) == ['spinach', 'carrots', 'artichoke',
                                        'celery', 'parsnips']


# Problem 3
def odd_products(num_lists):
    '''
    num_lists: a list of lists of numbers
    Returns: a list containing only the lists from num_lists whose length
             is odd, sorted by the product of the elements in each list, from
             highest product to lowest product.
    If a list contains a single value, that should be considered its product.
    If multiple lists have the same product, ties should be broken by the
    length of the list so that the longer list comes first. If multiple lists
    have the same length and the same product, then any order between them is
    fine. You may assume that num_lists contains at least one list, and that
    each inner list is non-empty and only contains integers.
    '''
    finding_odds = dict()
    # Keys: Product. Values: A list of odd lists that has this certain product
    for this_list in num_lists:
        if len(this_list) % 2 != 0:
            product = 1
            for num in this_list:
                product = product * num
            finding_odds.setdefault(product, [])
            finding_odds[product].append(this_list)

    product_decending = sorted(finding_odds.keys(), reverse=True)
    odds = []
    for key in product_decending:
        product_lengths = sorted(finding_odds[key], key=len, reverse=True)
        odds += product_lengths
    return odds


def test_odd_products():
    l1 = [[9, 1], [1, 3, 3], [0], [13, 2]]
    assert odd_products(l1) == [[1, 3, 3], [0]]
    l2 = [[1, 2, 3], [1, 2, 1, 3, 1]]
    assert odd_products(l2) == [[1, 2, 1, 3, 1], [1, 2, 3]]
    l3 = [[-1, 5, 1], [4], [-2, -2, 1]]
    assert odd_products(l3) == [[-2, -2, 1], [4], [-1, 5, 1]]
    l4 = [[0], [1, -33, 0], [0, 2]]
    assert odd_products(l4) == [[1, -33, 0], [0]]
    l5 = [[1, 1, 1, 1, -1], [10, 2, 1, 1], [2, 4, 1]]
    assert odd_products(l5) == [[2, 4, 1],  [1, 1, 1, 1, -1]]


def main():
    test_every_set()
    test_get_sorted_veggies()
    test_odd_products()


if __name__ == "__main__":
    main()
