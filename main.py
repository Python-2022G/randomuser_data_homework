import json


def first_user_name(data: dict) -> str:
    first_user = data['results'][0]
    first = first_user['name']['first']
    last = first_user['name']['last']
    title = first_user['name']['title']
    return f'{title} {first} {last}'



# print(first_user_name(data_dict))

# ['Mr Dominic Warholm', ..., ...]



def get_all_fullname(data: dict) -> list[str]:
    '''find all user name as list'''
    all_fullnames = []

    for user in data['results']:
        first = user['name']['first']
        last = user['name']['last']
        title = user['name']['title']

        fullname = f'{title} {first} {last}'
        all_fullnames.append(fullname)

    return all_fullnames



data_str = open('randomuser_data.json').read()
data_dict = json.loads(data_str)

print(get_all_fullname(data_dict))