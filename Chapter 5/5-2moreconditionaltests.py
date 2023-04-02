#5-2 More Conditional Tests
games = 'octopath traveler'
games == 'octopath traveler'

games = 'octopath traveler'
games == 'runescape'

games = 'Octopath Traveler'
games.lower() == 'octopath traveler'

age = 28
age == 28
age == 30
age <= 30
age >=30
age < 30
age > 30

age <= 30 and age >= 18

age_0 = 28
age_1 = 18
age_0 >=18 or age_1 <= 28

games = ['octopath traveler', 'runescape', 'dead cell']
'octopath traveler' in games


games = ['octopath traveler', 'runescape', 'dead cell']
game = 'octopath traveler 2'

if game not in games:
    print(f"{game.title()}, is not in our library")
if game in games:
    print(f"{game.title()}, is available in our library")