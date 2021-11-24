def multipleWrap(package):
    count = len(str(package)) - len(str(package).replace('[', ''))
    new_list = package
    if( count == 0 ): return 0
    for i in range(count-1):
        try:
            [new_list] = package
            package = new_list
        except:
            while(True):
                try:
                    [new_list] = package
                    package = new_list
                    break
                except:
                    if(new_list[0] == '['): count -= 1
                    if(type(new_list[0]) is list): del new_list[len(new_list)-1]
                    if(type(new_list[0]) is not list): del new_list[0]
    print(new_list)
    return count + len(new_list)

print(multipleWrap([["gfh","[",["wow","wow"],"wow"]]))