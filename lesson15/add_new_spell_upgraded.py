def add_new_spell(spells_list, *new_spell):
    z = True
    for i in new_spell:
        if i in spells_list:
            z = False
        else:
            spells_list.add(i)
    return z   
new_spell = ''
Harry = {'Accio', 'Wingardium Leviosa', 'Expelliarmus', 'Expecto patronum'}
Ron = {'Accio', 'Wingardium Leviosa', 'Alohomora'}
print(add_new_spell(Ron, 'Expecto patronum', 'avada kedavra'))