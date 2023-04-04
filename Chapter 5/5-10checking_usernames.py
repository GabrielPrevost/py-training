#5-10 Checking Usernames
current_users = ['prevg', 'jay', 'admin', 'maniiac1', 'silvaro']
new_users = ['pepper', 'barbue', 'meier', 'PREVG', 'warshine']

# Convert all current usernames to lowercase
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    # Convert the new username to lowercase before checking
    if new_user.lower() in current_users_lower:
        print(f"Sorry, the username {new_user} is already in use!")
    else:
        print(f"Success! {new_user} is available to use.")