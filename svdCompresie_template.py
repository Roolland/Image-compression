
# Nume student:Stoica Roland-Viorel
####################################
# DVS: Compresia de imagini alb negru
####################################

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Functie de conversie din RGB in GRAY
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])


#Cititi o imagine rgb la alagere
Img =  mpimg.imread('imagine.png') # remarca: matplotlib accepta doar imagini .png
fig1 =plt.figure(1)
plt.imshow(Img)

fig2 =plt.figure(2)
grayImg = rgb2gray(Img)
plt.imshow(grayImg, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)

# 1. Aplicati svd pe imaginea gray
(U,S,V) = np.linalg.svd(grayImg)

# 2. Plotati valorile singulare pe scala logaritmica utilizand plt.semilogy
fig3 = plt.figure(3)
plt.title("Valori singulare pe scala logaritmica")

plt.semilogy(S)
# Adaugati comentariu cu ce observati
# primele 300 de valori singulare sunt peste ordinul 1, iar restul valorilor vor deveni nesemnificative

# 3. Plotati graficul procent informatie vs valori singulare
# Hint: utilizati functia np.cumsum.
fig4 = plt.figure(4)
plt.title("procent informatie vs valori singulare")

plt.plot(np.cumsum(S) / np.sum(S))
plt.show()
# Adaugati comentariu cu ce observati
# peste 90% din informatie este retinuta in primele 231 de valori

# 4. In urma analizei graficului procent informatie vs valori singulare generati
# un vector de dimensiune minim 5. Utilizati elementele vectorului pentru a reconstrui imaginile
ranks = [5, 10, 50, 100, 200, 300]
ns = len(S)
j = 1

for i in ranks:
    fig5 = plt.figure(j)
    rang_img = U[:,:i] @ np.diag(S[:i]) @ V[:i,:]
    plt.imshow(rang_img, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
    j = j + 1;

plt.show()
