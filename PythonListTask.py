import sys
ages= [2, 12, 12, 14, 15, 16, 16, 17, 18, 14, 20, 20]
ages = list(dict.fromkeys(ages))
print(ages)
ages = max(ages)
print(ages)


ages=[2,12,12,14,15,16,16, 17,18, 14, 20, 20]
ages1=[2,4,12,14,15,16,16, 17,18, 14, 20, 20]


def same_age(ages, ages1):
    for num in ages:
        if num in ages1:
           return True
    return False

print(same_age([2,12,12,14,15,16,16, 17,18, 14, 20, 20], [2,4,12,14,15,16,16, 17,18, 14, 20, 20]))



######################################################################################################

# Get highest number in a list.
def get_max_number_v_1(my_list):
    return max(my_list)


# Get highest number in a list.
def get_max_number_v_2(my_list):
    return my_list.sort()[-1]


def remove_duplicates(my_list):
    return list(set(my_list))


ages = [2, 12, 12, 14, 15, 16, 16, 17, 18, 14, 20, 20]

print("Exercise 1. 30/09")
print("Max value in ", ages, "is(v1): ", get_max_number_v_1(ages))
print("Max value in ", ages, "is(v2): ", get_max_number_v_1(ages))
print("Removing duplicates in ", ages, ": ", remove_duplicates(ages))
print("")
print("Exercise 2. 30/09")


def compare_lists(list1, list2):
    for num in list1:
        if num in list2:
            return True
    return False


ages1 = [2, 12, 12, 14, 15, 16, 16, 17, 18, 14, 20, 20]
ages2 = [2, 4, 12, 14, 15, 16, 16, 17, 18, 14, 20, 20]

if compare_lists(ages1, ages2):
    print("The list(s) have at least one common member.")
else:
    print("The list(s) have no common  members.")


