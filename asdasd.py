def dni(dzien):
    dni = {"1": "poniedzialek", "2": "wtorek", "3": "sroda", "4": "czwartek", "5": "piatek", "6": "sobota",
           "7": "niedziela"}
    print(dni['' + str(dzien) + ''])

dni(4)


def palindrom(slowo):
    if (slowo == slowo[::-1]):
        return 1
    else:
        return 0

print(palindrom('kajak'))
print(palindrom('asd'))
