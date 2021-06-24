current_users = ['Oruj', 'jasmine', 'china', 'heydar', 'Maleyka']
new_users = ['imran', 'mehriban', 'jamal', 'maleyka', 'china']
current_users_lowercase = []

for current_user in current_users:
    current_users_lowercase.append(current_user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_lowercase:
        print(f"{new_user.title()}, you need to select new name.")
    else:
        print("This username is available.")
