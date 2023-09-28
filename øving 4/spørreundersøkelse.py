from sys import exit

antall_kvinner = 0
antall_menn = 0
antall_elever = 0
antall_ITGK = 0
antall_timer_lekser = 0

def sjekk_svar(spm, gyldige_svar):
    svar = input(spm).lower()
    while svar not in gyldige_svar:
        print("Ugyldig svar. Prøv igjen.")
        svar = input(spm).lower()
    return svar

def les_streng(spm):
    return input(spm)

def les_ja_nei(spm):
    return sjekk_svar(spm, ['ja', 'nei'])

def les_tall(spm):
    while True:
        try:
            return float(input(spm))
        except ValueError:
            print("Ugyldig tall. Prøv igjen.")

def skriv_statistikk():
    print("\nResultat av undersøkelse!")
    print("Antall kvinner:", antall_kvinner)
    print("Antall menn:", antall_menn)
    print("Antall personer som tar fag:", antall_elever)
    print("Antall personer som tar ITGK:", antall_ITGK)
    if antall_elever > 0:
        gjennomsnitt_timer_lekser = antall_timer_lekser / antall_elever
        print("Antall timer i snitt brukt på lekser:", gjennomsnitt_timer_lekser)

first = True
while True:
    if not first:
        avslutt = input("\nVil du avslutte undersøkelsen? (Skriv 'hade' for å avslutte, eller press enter for å fortsette: ")

        if avslutt.lower() == "hade":
            skriv_statistikk()
            exit()
    first = False

    print("\nVelkommen til spørreundersøkelsen!\n")

    # a
    kjonn = sjekk_svar("Hvilket kjønn er du? [f/m]: ", ['f', 'm'])

    if kjonn == 'f':
        antall_kvinner += 1
    else:
        antall_menn += 1



    # b
    alder = les_tall("Hvor gammel er du?: ")

    if alder < 16 or alder > 25:
        print("Du kan dessverre ikke ta denne undersøkelsen")
        continue

    # c
    fag = les_ja_nei("Tar du et eller flere fag? [ja/nei]: ")

    # d
    if fag == "ja":
        antall_elever += 1
        if alder < 22:
            itgk_spm = "Tar du ITGK? [ja/nei]: "

        else:
            itgk_spm = "Tar virkelig du ITGK? [ja/nei]: "

        medlem_ITGK = les_ja_nei(itgk_spm)
        antall_ITGK += 1 if medlem_ITGK == 'ja' else 0

        # e
        antall_timer_lekser += les_tall("Hvor mange timer bruker du daglig (i snitt) på lekser?: ")

