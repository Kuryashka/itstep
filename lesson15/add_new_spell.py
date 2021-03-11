def add_new_spell(spells_list: set, new_spell: str) -> bool:
    z = bool
    if new_spell in spells_list:
        z = False
    else:  
        z = True
        spells_list.add(new_spell)
    return z   
new_spell = ''
Harry = {'Accio', 'Wingardium Leviosa', 'Expelliarmus', 'Expecto patronum'}
Ron = {'Accio', 'Wingardium Leviosa', 'Alohomora'}
print(add_new_spell(Ron, 'Expecto patronum'))
print(Harry)