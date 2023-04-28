import gspread
import pandas as pd
import streamlit as st
import numpy as np
from datetime import datetime
from datetime import datetime, timedelta
from openpyxl import load_workbook
import matplotlib.pyplot as plt
import seaborn as sns
import openpyxl
import warnings
warnings.filterwarnings('ignore')

gc = gspread.service_account(filename='cred.json')

sheet1 = gc.open('Dashboard').worksheet('ARBOUR_INV')
sheet2 = gc.open('Dashboard').worksheet('ARBOUR_ADR')
sheet3 = gc.open('Dashboard').worksheet('ARBOUR_OCC')
sheet4 = gc.open('Dashboard').worksheet('ARBOUR_REV')

sheet5 = gc.open('Dashboard').worksheet('ALTERA_INV')
sheet6 = gc.open('Dashboard').worksheet('ALTERA_ADR')
sheet7 = gc.open('Dashboard').worksheet('ALTERA_OCC')
sheet8 = gc.open('Dashboard').worksheet('ALTERA_REV')

sheet9 = gc.open('Dashboard').worksheet('AMBERPTY_INV')
sheet10 = gc.open('Dashboard').worksheet('AMBERPTY_ADR')
sheet11 = gc.open('Dashboard').worksheet('AMBERPTY_OCC')
sheet12 = gc.open('Dashboard').worksheet('AMBERPTY_REV')

sheet13 = gc.open('Dashboard').worksheet('ARDEN_INV')
sheet14 = gc.open('Dashboard').worksheet('ARDEN_ADR')
sheet15 = gc.open('Dashboard').worksheet('ARDEN_OCC')
sheet16 = gc.open('Dashboard').worksheet('ARDEN_REV')

sheet17 = gc.open('Dashboard').worksheet('TG_INV')
sheet18 = gc.open('Dashboard').worksheet('TG_ADR')
sheet19 = gc.open('Dashboard').worksheet('TG_OCC')
sheet20 = gc.open('Dashboard').worksheet('TG_REV')

sheet21 = gc.open('Dashboard').worksheet('ASTER_INV')
sheet22 = gc.open('Dashboard').worksheet('ASTER_ADR')
sheet23 = gc.open('Dashboard').worksheet('ASTER_OCC')
sheet24 = gc.open('Dashboard').worksheet('ASTER_REV')

sheet25 = gc.open('Dashboard').worksheet('AMBER85_INV')
sheet26 = gc.open('Dashboard').worksheet('AMBER85_ADR')
sheet27 = gc.open('Dashboard').worksheet('AMBER85_OCC')
sheet28 = gc.open('Dashboard').worksheet('AMBER85_REV')

data1 = sheet1.get_all_values()
data2 = sheet2.get_all_values()
data3 = sheet3.get_all_values()
data4 = sheet4.get_all_values()

data5 = sheet5.get_all_values()
data6 = sheet6.get_all_values()
data7 = sheet7.get_all_values()
data8 = sheet8.get_all_values()

data9 = sheet9.get_all_values()
data10 = sheet10.get_all_values()
data11 = sheet11.get_all_values()
data12 = sheet12.get_all_values()

data13 = sheet13.get_all_values()
data14 = sheet14.get_all_values()
data15 = sheet15.get_all_values()
data16 = sheet16.get_all_values()

data17 = sheet17.get_all_values()
data18 = sheet18.get_all_values()
data19 = sheet19.get_all_values()
data20 = sheet20.get_all_values()

data21 = sheet21.get_all_values()
data22 = sheet22.get_all_values()
data23 = sheet23.get_all_values()
data24 = sheet24.get_all_values()

data25 = sheet25.get_all_values()
data26 = sheet26.get_all_values()
data27 = sheet27.get_all_values()
data28 = sheet28.get_all_values()

arb_inv = pd.DataFrame(data1[1:],columns=data1[0])
arb_adr = pd.DataFrame(data2[1:],columns=data2[0])
arb_occ = pd.DataFrame(data3[1:],columns=data3[0])
arb_rev = pd.DataFrame(data4[1:],columns=data4[0])

alt_inv = pd.DataFrame(data5[1:],columns=data5[0])
alt_adr = pd.DataFrame(data6[1:],columns=data6[0])
alt_occ = pd.DataFrame(data7[1:],columns=data7[0])
alt_rev = pd.DataFrame(data8[1:],columns=data8[0])

amp_inv = pd.DataFrame(data9[1:],columns=data9[0])
amp_adr = pd.DataFrame(data10[1:],columns=data10[0])
amp_occ = pd.DataFrame(data11[1:],columns=data11[0])
amp_rev = pd.DataFrame(data12[1:],columns=data12[0])

ard_inv = pd.DataFrame(data13[1:],columns=data13[0])
ard_adr = pd.DataFrame(data14[1:],columns=data14[0])
ard_occ = pd.DataFrame(data15[1:],columns=data15[0])
ard_rev = pd.DataFrame(data16[1:],columns=data16[0])

tg_inv = pd.DataFrame(data17[1:],columns=data14[0])
tg_adr = pd.DataFrame(data18[1:],columns=data18[0])
tg_occ = pd.DataFrame(data19[1:],columns=data19[0])
tg_rev = pd.DataFrame(data20[1:],columns=data20[0])

as_inv = pd.DataFrame(data21[1:],columns=data21[0])
as_adr = pd.DataFrame(data22[1:],columns=data22[0])
as_occ = pd.DataFrame(data23[1:],columns=data23[0])
as_rev = pd.DataFrame(data24[1:],columns=data24[0])

am85_inv = pd.DataFrame(data25[1:],columns=data25[0])
am85_adr = pd.DataFrame(data26[1:],columns=data26[0])
am85_occ = pd.DataFrame(data27[1:],columns=data27[0])
am85_rev = pd.DataFrame(data28[1:],columns=data28[0])


st.write(arb_inv)

