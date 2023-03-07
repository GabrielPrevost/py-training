#3-5 Changing Guest list
guests = ['raphie', 'audrey', 'serge', 'marie-claude']

print(f'This is an invitation to a dinner party for {guests[0].title()}.')
print(f'This is an invitation to a dinner party for {guests[1].title()}.')
print(f'This is an invitation to a dinner party for {guests[2].title()}.')
print(f'This is an invitation to a dinner party for {guests[3].title()}.')

cannot_attend = 'raphie'
print(f'{cannot_attend.title()}, cant come to the dinner party')

guests.remove(cannot_attend)
guests.insert(0, 'Raphaelle')

print(f'This is an invitation to a dinner party for {guests[0].title()}.')
print(f'This is an invitation to a dinner party for {guests[1].title()}.')
print(f'This is an invitation to a dinner party for {guests[2].title()}.')
print(f'This is an invitation to a dinner party for {guests[3].title()}.')
