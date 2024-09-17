'''
1. 
In `get_friends_favorite_candy_count()`, return a dictionary of candy names 
and the amount of times each candy appears in the `friend_favorites` list.

friend_favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
]
'''
# friend_favorites = [
#     ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
#     ["Bob", ["milky way", "licorice", "lollipop" ]],
#     ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
#     ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
# ]


def get_friends_favorite_candy_count(favorites):
    candy_names = {}
    for friend in favorites:
        for candy in friend[1]:
            if candy not in candy_names.keys():
                candy_names[candy] = 1
            else:
                candy_names[candy] += 1
    return candy_names

# print(get_friends_favorite_candy_count(friend_favorites))

'''
2. 
Given the list `friend_favorites`, create a new data structure in the 
function `create_new_candy_data_structure` that describes the different 
kinds of candy paired with a list of friends that like that candy. 

friend_favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
]
'''
def create_new_candy_data_structure(data):
    candy_pairs = {}
    favorite_candies = get_friends_favorite_candy_count(data)

    for candies in favorite_candies.keys():
        for student in data:
            if candies in student[1]:
                candy_pairs[candies] = student[0]
    return candy_pairs

   
                    




    

'''
3. 
In `get_friends_who_like_specified_candy()`, return a tuple of 
friends who like the candy specified in the candy_name parameter.
'''
def get_friends_who_like_specific_candy(data, candy_name):
    pass

'''
4. 
In, `create_candy_set()`, return a set of all the candies from
the data structure made in `create_new_candy_data_structure()`.
'''
def create_candy_set(data):
    pass 

'''
5. 
Starting with nominal cases, write tests for each of the functions 
in the file tests/test_candy_data_structure.py then write tests to 
handle edge cases.
'''

