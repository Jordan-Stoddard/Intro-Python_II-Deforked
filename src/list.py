int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#lc = [FORMATTING     COLLECTION    CONDITION]
#lc = [MAP     COLLECTION    FILTER]

# add 3 to each number

add_3_list = [(i + 3)    for i in int_list     ]


add_3_list_to_odds_list = [i    for i in int_list     if i == 3]
print(add_3_list_to_odds_list)

make_evens_strings_list = [str(i)    for i in int_list     if i % 2 == 0]




