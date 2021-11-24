def villageAttack(textVillage, lstKiller):
    killer = {
        "spear" : lambda tmpcheck: False if tmpcheck.count('=') == 0 else True,
        "arrow" : lambda tmpcheck: False if tmpcheck.count('^') == 0 else True,
        "winter": lambda tmpcheck: False if tmpcheck.count('0') == 0 else True,
        "flood" : lambda tmpcheck: False if tmpcheck.count('0') > 0 else True
    }
    survi = ""
    lstsurvi = []
    for i in range(0, len(textVillage) ):
        if i == len(textVillage)-1 : survi += textVillage[i]
        if(textVillage[i] == '(' and i != 0 or i == len(textVillage)-1):
            for k in lstKiller:
                if killer[k](survi): check = True
                else : 
                    check = False
                    break
            if check : lstsurvi.append(survi)
            survi = ""
        survi += textVillage[i]
    survi = ""
    return survi.join(lstsurvi)
print(villageAttack('() (0) (0) ^ () = (0) ^= () (0) =',['winter']))
print(villageAttack('(0) = () ^= (0) =^ () ^',['arrow', 'spear']))
print(villageAttack('(0) = () ^= (0) =^ () ^ (0) () () =^', ['arrow', 'spear', 'flood']))