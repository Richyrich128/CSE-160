# Name: Richard Castro
# CSE 160
# Autumn 2020
# Midterm Exam


# Problem 1
def check_sort(nums, first, second):
    '''
    nums - a list of integers
    first, second - valid indexes into nums
    Assume first =< second
    Returns True if numbers in nums between position first (inclusive)
    and second (exclusive) are sorted in ascending order.
    Return True if nums is empty or if first and second are equal.
    Return False otherwise.
    '''
    if not nums or first == second:
        return True
    f = nums[first]

    for i in range(second - first - 1):
        if (nums[first + i + 1] > f):
            f = nums[first + i]
        else:
            return False
    return True


assert check_sort([10, 12, 13, 14, 5], 1, 4) is True
assert check_sort([10000, 2, 1, 2, 3, 10000], 0, 5) is False
assert check_sort([], 0, 0) is True


# Problem 2
def class_standing(lst):
    '''
    lst - a list of lists of integers representing credit hours
    The function will sum up the integers in all lists contained in lst.
    Returns a string:
    “freshman” if the student has less than 45 credits total,
    “sophomore” if they have at least 45 credits and less than 90 credits,
    "junior" if they have at least 90 credits and less than 135 credits, and
    “senior” if they have 135 credits or more
    '''
    credits = 0
    index = len(lst)
    for i in range(index):
        if not lst[0]:
            return "freshman"
        courses = len(lst[i])
        list = lst[i]
        for j in range(courses):
            credits += list[j] 
    if credits < 45:
        return "freshman"
    elif credits < 90:
        return "sophomore"
    elif credits < 135:
        return "junior"
    else:
        return "senior"


assert class_standing([[]]) == "freshman"
assert class_standing([[5, 5], [3, 1, 2], [10]]) == "freshman"
assert class_standing([[5, 5, 5], [4, 5, 5, 1], [5, 5, 5, 1],
                       [4, 4, 3, 1], [5, 5, 4], [3, 2, 5, 3]]) == "sophomore"


# Problem 3
def verify_lengths(words, min, max):
    '''
    words - a list of strings
    min, max - positive integers where min <= max
    Returns True if all strings in words have a
    length between min and max (both inclusive).
    Return False otherwise.
    Return False if words is an empty list.
    '''
    if not words:
        return False
    for k in range(len(words)):
        if len(words[k]) < min or len(words[k]) > max:
            return False
    return True


assert verify_lengths([], 2, 3) is False
assert verify_lengths(["cats", "are", "cool"], 3, 4) is True
assert verify_lengths(["12345", "12345", "12", "1"], 2, 5) is False


# Problem 4
def weave_max(list1, list2):
    '''
    list1, list2 - non-empty lists of numbers
    Returns a new list that contains the larger of the first numbers in list1
    and list2, followed by the larger of the second numbers in list1 and
    list2, etc. until one of the two lists runs out. After one of the lists
    runs out, the remaining numbers from the longer list should be appended to
    the new list.
    '''
    new_list = []
    shorter = 0
    bigger = ""
    if len(list1) < len(list2):
        shorter = len(list1)
        bigger = list2
    else:
        shorter = len(list2)
        bigger = list1

    for q in range(shorter):
        if list1[q] <= list2[q]:
            new_list.append(list2[q])
        else:
            new_list.append(list1[q])
    
    for w in range(abs(len(list1) - len(list2))):
        new_list.append(bigger[w + shorter])
    return new_list

assert weave_max([1, 54, 6, 8], [2, 3, 7, 11, 9, 1]) == [2, 54, 7, 11, 9, 1]
assert weave_max([1], [2]) == [2]


# Problem 5
def star_changer(word):
    '''
    word - a string
    Returns a new string with stars (*) substituted for every other character,
    starting with the second character.
    The number of stars in the new string should match the index of the
    character you are replacing.
    '''
    new_string = ""
    for y in range(len(word)):
        
        if y % 2 != 0:
            for in range(y):
                new_string += "*"
        else:
            new_string += word[y]

    return new_string

assert star_changer("star") == "s*a***"
assert star_changer("one") == "o*e"
assert star_changer("") == ""
assert star_changer("a") == "a"
assert star_changer("  ") == " *"
assert star_changer("long word") == "l*n*** *****o*******d"

# ANSWER the following questions as COMMENTS

# (1 pt) Did you work on this quiz alone or collaborate with others?
# Calaborate with 2 others

# If you collaborated with others, list full names and UWNetIDs
# of everyone you collaborated with.
''' 
Steven Nguyen and ID: stevenn1
Maya leshikar and ID: mayal3
'''