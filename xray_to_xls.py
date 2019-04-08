import numpy as np
import pandas as pd
from imageio import imread
from skimage import data
import matplotlib.pyplot as plt

#loading image
#carregando o arquivo
photo_data = imread("./xray.jpg")
im = np.array(photo_data[:,:,0])

#"plotting image"
#"plotando" a imagem
plt.imshow(im)
plt.show()
print(im.shape)

# Saving as Excel file:
# Salvando como Excel:
pd.DataFrame(im).to_excel('xray.xlsx',index=False,header=False)

# No excel, ajuste a largura das células (auto-ajuste da largura)
# e ative a formatação condicional das célulcas, por cores.

# In Excel, make an auto-adjust of cell width, and activate 
# conditional cell formatting for collors. 

# Have fun! :D