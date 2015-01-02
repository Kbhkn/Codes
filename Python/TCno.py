def tcno_checksum(tcno):
    if len(str(tcno)) == 9:
        tc    = '%d' % tcno
        tc10  = int(tc[0]) + int(tc[2]) + int(tc[4]) + int(tc[6]) + int(tc[8])
        tc10 *= 7
        tc10 -= int(tc[1]) + int(tc[3]) + int(tc[5]) + int(tc[7])
        tc10 %= 10
        tc11  = int(tc[0]) + int(tc[1]) + int(tc[2]) + int(tc[3]) + int(tc[4])
        tc11 += int(tc[5]) + int(tc[6]) + int(tc[7]) + int(tc[8]) + int(tc10)
        tc11 %= 10
        return '%s%d%d' % (tc, tc10, tc11)
    else:
        return 0

def akraba_tcno(tcno, adet):
    akraba_liste = ''
    Liste = []
    tc   = int(tcno[0:-2])
    t    = tc - 29999 * (1 + int(adet / 2))
    for i in range(adet+1):
        t += 29999
        atc = tcno_checksum(t)
        if atc == tcno:
            pass
        else:
            akraba_liste += "'%s'," % atc
            #if int(atc) > 25600000000 and int(atc)<25700000000:
            #    Liste.append(int(atc))
    #print(Liste)
    return akraba_liste[0:-1]

#print(tcno_checksum(279623605))
print(akraba_tcno('40039361680',1000))
#akraba_tcno('25490502322',1000)
