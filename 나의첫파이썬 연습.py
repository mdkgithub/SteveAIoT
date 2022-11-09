# favorite_languages = {
#     'jen':['python', 'ruby'],
#     'sarah':['c'],
#     'edward':['ruby','go'],
#     'phil':['python','haskell']
# }
#
# for name, languages in favorite_languages.items():
#     print(f"\n{name.title()}'s favorite languages are:")
#     for language in languages:
#             print(f"\t{language.title()}")


# users = {
#     'aeistein':{
#         'first':'albert',
#         'last':'einstein',
#         'location':'princerton',
#     },
#     'mcurie':{
#         'first':'marie',
#         'last':'curie',
#         'location':'paris'
#     },
# }
#
# for username, user_info in users.items():
#     print(f"\nUsername: {username}")
#     # full_name = f"{user_info['first']} {user_info['last']}"
#     full_name = user_info['first'] + user_info['last']
#     location = user_info['location']
#
#     print(f"\tFull name: {full_name.title()}")
#     # print(f"\tFull name: {full_name}")
#     # print(f"\tLocation: {location.title()}")
#     print(f"\tLocation: {location}")


orders = [{'user_id':123, 'products':['a','c']},
         {'user_id':125, 'products':['e']},
         {'user_id':124, 'products':['b','d','e']}]


for u_id, ps in orders:
    # print(u_id)
    for number in u_id:
        print(number)
