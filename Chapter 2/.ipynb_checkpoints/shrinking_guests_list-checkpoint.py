#Shrinking Guest List
guests = ['raphie', 'audrey', 'serge', 'marie-claude']

print(f'This is an invitation to a dinner party for {guests[0].title()}.')
print(f'This is an invitation to a dinner party for {guests[1].title()}.')
print(f'This is an invitation to a dinner party for {guests[2].title()}.')
print(f'This is an invitation to a dinner party for {guests[3].title()}.')

cannot_attend = 'raphie'
print(f'\n{cannot_attend.title()}, cant come to the dinner party')

guests.remove(cannot_attend)
guests.insert(0, 'raphaelle')

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

print(f'\nUnfortunately only 2 of you guys can come to the dinner')
uninvited_guests = guests.pop()
print(f'\nSorry {uninvited_guests.title()}')
uninvited_guests = guests.pop()
print(f'Sorry {uninvited_guests.title()}')
uninvited_guests = guests.pop()
print(f'Sorry {uninvited_guests.title()}')
uninvited_guests = guests.pop()
print(f'Sorry {uninvited_guests.title()}')
uninvited_guests = guests.pop()
print(f'Sorry {uninvited_guests.title()}')

print(f'\nHello {guests[0].title()} and {guests[1].title()}, this is going to be only us 3 for dinner')

del guests[0]
del guests[0]
print(guests)