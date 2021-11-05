import numpy as np
import pandas as pd
import matplotlib.pyplot as pl
import scipy.stats as stats
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import seaborn as sns
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.model_selection import train_test_split
from datetime import datetime
from sklearn.metrics import accuracy_score
from sklearn import tree
from sklearn.metrics import r2_score
import pickle
from datetime import date


def return_prediction_simple(df_cd, df_no):
	today = date.today()

	df_no['weeknr'] = f"weeknr_w{today.isocalendar()[1]}"

	all_dummies = ['weeknr_w1',
				   'weeknr_w10',
				   'weeknr_w11',
				   'weeknr_w12',
				   'weeknr_w13',
				   'weeknr_w14',
				   'weeknr_w15',
				   'weeknr_w16',
				   'weeknr_w17',
				   'weeknr_w18',
				   'weeknr_w19',
				   'weeknr_w2',
				   'weeknr_w20',
				   'weeknr_w21',
				   'weeknr_w22',
				   'weeknr_w23',
				   'weeknr_w24',
				   'weeknr_w25',
				   'weeknr_w26',
				   'weeknr_w27',
				   'weeknr_w28',
				   'weeknr_w29',
				   'weeknr_w3',
				   'weeknr_w30',
				   'weeknr_w31',
				   'weeknr_w32',
				   'weeknr_w33',
				   'weeknr_w34',
				   'weeknr_w35',
				   'weeknr_w36',
				   'weeknr_w37',
				   'weeknr_w38',
				   'weeknr_w39',
				   'weeknr_w4',
				   'weeknr_w40',
				   'weeknr_w41',
				   'weeknr_w42',
				   'weeknr_w43',
				   'weeknr_w44',
				   'weeknr_w45',
				   'weeknr_w46',
				   'weeknr_w47',
				   'weeknr_w48',
				   'weeknr_w49',
				   'weeknr_w5',
				   'weeknr_w50',
				   'weeknr_w51',
				   'weeknr_w52',
				   'weeknr_w53',
				   'weeknr_w6',
				   'weeknr_w7',
				   'weeknr_w8',
				   'weeknr_w9',
				   'Oorzaak_Aanrijding (bijna) tijdens werkzaamheden',
				   'Oorzaak_Afstelling onjuist/verlopen',
				   'Oorzaak_Applicatie/softwarefout',
				   'Oorzaak_Belemmerende vegetatie',
				   'Oorzaak_Bij onderzoek in orde/geen oorzaak gevonden',
				   'Oorzaak_Bijna aanrijding met persoon langs baan',
				   'Oorzaak_Bijna aanrijding met wegverkeer',
				   'Oorzaak_Braamvorming',
				   'Oorzaak_Brand(alarm), bommelding, gevaar/explosie',
				   'Oorzaak_Breuk/scheurvorming/afbrokkeling',
				   'Oorzaak_Corrosie/aantasting',
				   'Oorzaak_Defect bijzonder voertuig tijdens transport',
				   'Oorzaak_Diefstal',
				   'Oorzaak_Dieren, schade door of (bijna) aanrijding',
				   'Oorzaak_Doorbranden',
				   'Oorzaak_EMC/bliksem',
				   'Oorzaak_Extreem hoge temperatuur',
				   'Oorzaak_Extreem lage temperatuur',
				   'Oorzaak_Fabricagefout',
				   'Oorzaak_Geen onderzoek',
				   'Oorzaak_Gladde sporen (bladval/chemicalien)',
				   'Oorzaak_Golfslijtage',
				   'Oorzaak_Groefvorming',
				   'Oorzaak_IJsafzetting/ijzel',
				   'Oorzaak_In- en uitzetten materieel',
				   'Oorzaak_Ingebrand/verbrand',
				   'Oorzaak_Inrijden',
				   'Oorzaak_Isolatie',
				   'Oorzaak_Katterug',
				   'Oorzaak_Klapper',
				   'Oorzaak_Kortsluiten',
				   'Oorzaak_Lekkage',
				   'Oorzaak_Levering nutsbedrijf: elek/gas/water/tel',
				   'Oorzaak_Montagefout',
				   'Oorzaak_Niet gemeld',
				   'Oorzaak_Omhoog werken/verschuiven',
				   'Oorzaak_Onderdeel defect door onbekende oorzaak',
				   'Oorzaak_Ondeskundig gebruik derden (bediening)',
				   'Oorzaak_Ongepland werk',
				   'Oorzaak_Onjuiste geometrie/ligging/blinde vering',
				   'Oorzaak_Onvoldoende onderhoud',
				   'Oorzaak_Onvoldoende smering',
				   'Oorzaak_Openrijden/kapotrijden',
				   'Oorzaak_Overbelasting',
				   'Oorzaak_Overig derden',
				   'Oorzaak_Overig processen',
				   'Oorzaak_Overig technisch',
				   'Oorzaak_Overspanning',
				   'Oorzaak_Pekel/zout',
				   'Oorzaak_RCF (headcheck)',
				   'Oorzaak_Regen/vocht/wateroverlast',
				   'Oorzaak_Schade door weg-/werk-/waterverkeer',
				   'Oorzaak_Slijtage',
				   'Oorzaak_Sneeuw/hagel',
				   'Oorzaak_Storm',
				   'Oorzaak_Systeemfout',
				   'Oorzaak_Trillingen',
				   'Oorzaak_Uitloop treinvrije periode',
				   'Oorzaak_Uitwalsing',
				   'Oorzaak_Vandalisme',
				   'Oorzaak_Vastgelopen',
				   'Oorzaak_Verbogen/vervormd',
				   'Oorzaak_Veroudering',
				   'Oorzaak_Verrot',
				   'Oorzaak_Vervuiling (derden)',
				   'Oorzaak_Vervuiling (technisch)',
				   'Oorzaak_Verzakking/klink/zetting',
				   'Oorzaak_Vreemd voorwerp',
				   'Oorzaak_Werkzaamheden']

	dummie_df = pd.DataFrame({x: [0] for x in all_dummies})

	nom_vals = [df_no['weeknr'].loc[0], df_no['Oorzaak'].loc[0]]

	for x in nom_vals:
		dummie_df[x] = 1

	df = df_cd.join(dummie_df)

	filename = 'webapp/ml_algorithms/mini_decision_tree.sav'

	clf = pickle.load(open(filename, 'rb'))

	pred = clf.predict(df)[0]

	print(df.loc[0][:5])

	return (f'{0 + (pred * 5)} - {5 + (pred * 5)}')

# stm_reactie_duur = 200
# stm_prioriteit = 7
# stm_km_tot_mld = 50
#
# data = ['stm_prioriteit', 'stm_reactie_duur', 'stm_km_tot_mld']
# df_cd = pd.DataFrame(data={v: [eval(v)] for v in data})
#
# Oorzaak = 'Oorzaak_Levering nutsbedrijf: elek/gas/water/tel'
#
# data = ['Oorzaak']
# df_no = pd.DataFrame({v: [eval(v)] for v in data})
#
#
# print(return_prediction_simple(df_cd, df_no))
