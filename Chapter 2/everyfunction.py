#3-10 Every Function
games = ['runescape', 'league of legends', 'world of warcraft']

print(games)

games.append('call of duty')

print(games)

games.insert(0, 'fortnite')

print(games)

games.remove('fortnite')

print(games)

popped_games = games.pop()
print(games)

del games[0]
print(games)

games.append('call of duty')
games.append('fortnite')
games.append('runescape')
print(games)

print(sorted(games))

games.sort()
print(games)

games.sort(reverse=True)
print(games)

games.reverse()
print(games)