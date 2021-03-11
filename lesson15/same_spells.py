def same_spells(ron_spells: set, harry_spells: set) -> set:
    return ron_spells.intersection(harry_spells)


ron = {'Accio', 'Wingardium Leviosa', 'Expelliarmus', 'Expecto patronum'}
harry = {'Accio', 'Wingardium Leviosa', 'Alohomora'}
print(same_spells(ron, harry))