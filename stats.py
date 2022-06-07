def stats(filename):
  f = open(filename,"rb")
  l = list(f.read())
  lenList = len(l)
  simplets = [0,0]
  doublets = [0,0,0,0]
  quadruplets = []
  octets = []

  #initialisation des tableaux de compteurs
  for i in range (0, 2**4):
    quadruplets.append(0)
  for i in range (0, 2**8):
    octets.append(0)

  #comptage des simplets, doublets, quadruplets et octets
  for i in range (0, lenList):
    octets[l[i]] += 1
    nb = convertDec2Bin(l[i], 8)
    for j in [0, 4]:
      simplets[nb[j]] += 1
      
      tmpD = nb[j]
      j += 1
      tmpD = tmpD * 2 + nb[j]
      
      simplets[nb[j]] += 1
      doublets[tmpD] += 1

      j += 1
      tmpQ = tmpD * 2 + nb[j]
      tmpD = nb[j]

      simplets[nb[j]] += 1

      j += 1
      tmpD = tmpD * 2 + nb[j]
      tmpQ = tmpQ * 2 + nb[j]

      simplets[nb[j]] += 1
      doublets[tmpD] += 1
      quadruplets[tmpQ] += 1

  #affichage simplets
  print("\nSimplets")
  for i in range (0, len(simplets)):
    simplets[i] = simplets[i] / (lenList * 8) * 100
    print(i,": {0:.2f}%".format(simplets[i]))

  #affichage doublets
  print("\nDoublets")
  for i in range (0, len(doublets)):
    doublets[i] = doublets[i] / (lenList * 4) * 100
    print(convertDec2Bin(i,2),": {0:.2f}%".format(doublets[i]))

  #affichage quadruplets
  print("\nQuadruplets")
  for i in range (0, len(quadruplets)):
    quadruplets[i] = quadruplets[i] / (lenList * 2) * 100
    print(convertDec2Bin(i,4),": {0:.2f}%".format(quadruplets[i]))

  #affichage octets
  print("\nOctets")
  for i in range(0, len(octets)):
    octets[i] = octets[i] / lenList * 100
    print(i,": {0:.2f}%".format(octets[i]))
  
  f.close()


def convertDec2Bin(nb, nbBits):
  i = 2 ** (nbBits - 1)
  tab = []
  
  while i:
    if nb & i:
      tab.append(1)
    else:
      tab.append(0)
    i >>= 1
  
  return tab