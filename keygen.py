



def keygen(x, r, size):


    key = []

    for i in range(size):

        x = r * x * (1 - x) # Formule de la logistic map (à changer si besoin)

        key.append(int((x * pow(10, 16)) % 256))


    return key

