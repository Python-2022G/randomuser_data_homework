from get_data import get_data

def get_email(data:dict) -> list:
    """
    Take the email of the users and return the list.

    Args:
        data(dict): data
    Returns:
        list: users email
    """
    emails = []
    for user in data['results']:
        emails.append(user['email'])
    
    return emails
    




dt = get_data('randomuser_data.json')
print(get_email(dt))