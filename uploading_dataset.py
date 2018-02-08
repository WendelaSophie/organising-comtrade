import numpy as np
import pandas as pd

pd.set_option('display.width', 350)

import warnings
warnings.filterwarnings('ignore')

zwe_file = '/Users/wendela/Dropbox/documents_wendela/work/general_datasets/comtrade/zwe.csv'
zwe = pd.read_csv(zwe_file, sep=',', index_col=False)

zwe = zwe.drop(['Period', 'Period Desc.','2nd Partner Code', '2nd Partner', '2nd Partner ISO', 'Customs Proc. Code',
                'Customs','Mode of Transport Code','Mode of Transport', 'Qty','Alt Qty Unit Code', 'Alt Qty',
                'Gross weight (kg)','CIF Trade Value (US$)', 'FOB Trade Value (US$)'], axis=1)

zwe['HS 2'] = zwe['Commodity Code']
zwe['HS 4'] = zwe['Commodity Code']
zwe['HS 6'] = zwe['Commodity Code']

zwe['HS 2'] = zwe['HS 2'].astype(str)
zwe['HS 4'] = zwe['HS 4'].astype(str)
zwe['HS 6'] = zwe['HS 6'].astype(str)

####################################

for i in range(0, len(zwe)):
    
    if len(str(zwe['HS 6'][i]))== 6:
        zwe['HS 2'].replace(to_replace=zwe['HS 2'][i], value='hs_'+zwe['HS 2'][i][0:2], inplace=True)
        zwe['HS 4'].replace(to_replace=zwe['HS 4'][i], value='hs_'+zwe['HS 4'][i][0:4], inplace=True)
        zwe['HS 6'].replace(to_replace=zwe['HS 6'][i], value='hs_'+zwe['HS 6'][i], inplace=True)
  
    elif (len(str(zwe['HS 6'][i])) == 5) & (zwe['HS 2'][i] != 'TOTAL'):
        zwe['HS 2'].replace(to_replace=zwe['HS 2'][i], value='hs_0'+zwe['HS 2'][i][0:1], inplace=True)
        zwe['HS 4'].replace(to_replace=zwe['HS 4'][i], value='hs_0'+zwe['HS 4'][i][0:3], inplace=True)
        zwe['HS 6'].replace(to_replace=zwe['HS 6'][i], value='hs_0'+zwe['HS 6'][i], inplace=True)
        
    elif len(str(zwe['HS 6'][i])) == 4:
        zwe['HS 2'].replace(to_replace=zwe['HS 2'][i], value='hs_'+zwe['HS 2'][i][0:2], inplace=True)
        zwe['HS 4'].replace(to_replace=zwe['HS 4'][i], value='hs_'+zwe['HS 4'][i], inplace=True)
        zwe['HS 6'].replace(to_replace=zwe['HS 6'][i], value='hs_'+zwe['HS 6'][i]+'00', inplace=True)
        
    elif len(str(zwe['HS 6'][i])) == 3:
        zwe['HS 2'].replace(to_replace=zwe['HS 2'][i], value='hs_0'+zwe['HS 2'][i][0:1], inplace=True)
        zwe['HS 4'].replace(to_replace=zwe['HS 4'][i], value='hs_0'+zwe['HS 4'][i], inplace=True)
        zwe['HS 6'].replace(to_replace=zwe['HS 6'][i], value='hs_0'+zwe['HS 6'][i]+'00', inplace=True)
        
    elif len(str(zwe['HS 6'][i])) == 2:
        zwe['HS 2'].replace(to_replace=zwe['HS 2'][i], value='hs_'+zwe['HS 2'][i], inplace=True)
        zwe['HS 4'].replace(to_replace=zwe['HS 4'][i], value='hs_'+zwe['HS 4'][i]+'00', inplace=True)
        zwe['HS 6'].replace(to_replace=zwe['HS 6'][i], value='hs_'+zwe['HS 6'][i]+'0000', inplace=True)

    elif len(str(zwe['HS 6'][i])) == 1:
        zwe['HS 2'].replace(to_replace=zwe['HS 2'][i], value='hs_0'+zwe['HS 2'][i], inplace=True)
        zwe['HS 4'].replace(to_replace=zwe['HS 4'][i], value='hs_0'+zwe['HS 4'][i]+'00', inplace=True)
        zwe['HS 6'].replace(to_replace=zwe['HS 6'][i], value='hs_0'+zwe['HS 6'][i]+'0000', inplace=True)
  
