def calculateFine(start, end):
    fine = 0
    lstart= list(map(int ,start.split(' ')))
    lend = list(map(int ,end.split(' ')))

    if lstart[2] > lend[2]:
        fine = 10000
    elif lstart[2] == lend[2]:
        if lstart[1] > lend[1]:
            fine += (int(lstart[1]) - int(lend[1])) * 500
        else:
            if lstart[0] > lend[0]:
                fine += (int(lstart[0]) - int(lend[0])) * 15
            else:
                fine = 0
    else:
        fine = 0
    return fine

actualDate = input()
expectedDate = input()

print(calculateFine(actualDate, expectedDate))

            