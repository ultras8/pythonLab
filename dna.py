def dna( dnaData ):
    lst = []
    if( dnaData.count("AUG") == 0 ): return lst
    for i in range(2,len(dnaData)):
        if(dnaData[i] == 'G' and dnaData[i-1] == 'U' and  dnaData[i-2] == 'A'):
            tmpstr = ""
            for j in range(i+1,len(dnaData)-1):
                if(dnaData[j] == 'U' and stop(dnaData, j)):
                    i = j+3
                    lst.append(tmpstr)   
                    break
                if(dnaData[j] == 'G' and dnaData[j-1] == 'U' and  dnaData[j-2] == 'A'):
                    tmpstr = ""
                    break
                tmpstr += dnaData[j]
    return lst
def stop(dnaData, j):
    if(dnaData[j+1] == 'A' and dnaData[j+2] == 'G'): return True
    if(dnaData[j+1] == 'A' and dnaData[j+2] == 'A'): return True
    if(dnaData[j+1] == 'G' and dnaData[j+2] == 'A'): return True
    return False

print( dna ('AUGAAAAAUAA') )
print( dna ('UAGUGAUAAUAGUGAUAA') )
print( dna ('AUGUUUUAUGUUUUUUAGUAAGGAUGGGGGGUGAAUG') )