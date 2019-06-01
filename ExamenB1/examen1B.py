# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 10:11:55 2019

@author: Alejo
"""

import pandas as pd
import numpy as np
 
# Pregunta 11
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))

serie_mylist = pd.Series(mylist)
serie_myarr = pd.Series(myarr)
serie_mydict = pd.Series(mydict)
print(type(serie_mylist))

#Pregunta 12
import pandas as pd
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
ser = pd.Series(mydict)

df_serie = pd.DataFrame(ser)
df_serie = columns['Indice']


# Pregunta 13
import numpy as np
import pandas as pd
ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))

serie_unidas = pd.concat([ser1,ser2])

# Pregunta 14
import numpy as np
import pandas as pd

ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])
ser_unidas = pd.concat([ser1,ser2])
unicos = pd.unique(ser_unidas)
# Pregunta 15



# Pregunta 16
import numpy as np
import pandas as pd

ser = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))
df_ser = pd.DataFrame(ser)
valores_repetidos = df_ser.groupby(df_ser.columns.tolist(), as_index=False).size()