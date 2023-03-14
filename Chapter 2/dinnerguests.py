#3-9 Dinner Guests
guests = ['raphie', 'audrey', 'serge', 'marie-claude']

print(f'This is an invitation to a dinner party for {guests[0].title()}.')
print(f'This is an invitation to a dinner party for {guests[1].title()}.')
print(f'This is an invitation to a dinner party for {guests[2].title()}.')
print(f'This is an invitation to a dinner party for {guests[3].title()}.')

cannot_attend = 'raphie'
print(f'\n{cannot_attend.title()}, cant come to the dinner party')

guests.remove(cannot_attend)
guests.insert(0, 'Raphaelle')

print(f'\nThis is an invitation to a dinner party for {guests[0].title()}.')
print(f'This is an invitation to a dinner party for {guests[1].title()}.')
print(f'This is an invitation to a dinner party for {guests[2].title()}.')
print(f'This is an invitation to a dinner party for {guests[3].title()}.')

print('\nHello everyone! I found a bigger table for our dinner party so i will add guests')
guests.insert(0, 'nico')
guests.insert(2, 'rosalie')
guests.append('juliette')

print(f'\nThis is an invitation to a dinner party for {guests[0].title()}.')
print(f'This is an invitation to a dinner party for {guests[1].title()}.')
print(f'This is an invitation to a dinner party for {guests[2].title()}.')
print(f'This is an invitation to a dinner party for {guests[3].title()}.')
print(f'This is an invitation to a dinner party for {guests[4].title()}.')
print(f'This is an invitation to a dinner party for {guests[5].title()}.')
print(f'This is an invitation to a dinner party for {guests[6].title()}.')
len(guests)