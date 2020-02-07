def pocet_kroku(schody, krok, vysky_schodu):
    reseni = 0

    curr_dist = 0
    for i in range(len(vysky_schodu)):
        curr_dist += vysky_schodu[i]

        if curr_dist > krok:
            break

        reseni += pokus(krok, vysky_schodu, i, 1)

    return reseni


def pokus(krok, schody, curr_schod,first_run=False):
    if first_run == 1:
        print("First run")
        print(schody[curr_schod])
    if first_run == 2:
        print("Second run")
        print(schody[curr_schod])
    if first_run == 3:
        print("Third run")
        print(schody[curr_schod])
    if first_run == 4:
        print("Fourth run")
        print(schody[curr_schod])
    reseni = 0
    globi = 0

    curr_dist = 0

    for i in range(curr_schod+1, len(schody)):
        curr_dist += schody[i]
        globi = i

        if curr_dist > krok:
            break

        reseni += pokus(krok, schody, i, first_run+1)

    if globi == len(schody)-1:
        reseni += 1

    if schody[curr_schod] == 4:
        print("----")
    return reseni

print(pocet_kroku(4, 100, [1, 2, 3, 4]))
