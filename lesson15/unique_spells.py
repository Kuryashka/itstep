def unique_spells(ron_spells: set, harry_spells: set) -> set:
    return ron_spells.symmetric_difference(harry_spells)


ron = {'Accio', 'Wingardium Leviosa', 'Expelliarmus', 'Expecto patronum'}
harry = {'Accio', 'Wingardium Leviosa', 'Alohomora'}
print(unique_spells(ron, harry))