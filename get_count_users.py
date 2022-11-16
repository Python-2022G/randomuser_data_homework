from get_data import get_data as gt

def get_count_users(data:dict) -> int:
    """
    You are given dictionary. Find the number of users.

    Args:
        data(dict): data
    Returns:
        int: number of users
    """
    users = len(data['results'])
    return users
    

data = gt('randomuser_data.json')

print(get_count_users(data))
