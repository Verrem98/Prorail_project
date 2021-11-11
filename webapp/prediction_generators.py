import pandas as pd
import pickle
from datetime import date
import numpy as np

def get_graph_data(prob_list):

	"""
	returns a list of 3 lists:
	list 1: list of color hexcodes
	list 2: list of bin probabilities sorted desc
	list 3: names of bins

	"""


	prob_dict = {(i+1): prob_list[i] for i in range(len(prob_list))}
	prob_dict = {k: v for k, v in sorted(prob_dict.items(), key=lambda item: item[1], reverse=True)}



	labels = list([f'{0 + ((i-1) * 5)} - {5 + ((i-1) * 5)} min' for i in prob_dict.keys()])[:3]
	labels.append('Overig')

	data = list(prob_dict.values())[:3]
	data.append(sum(list(prob_dict.values())[3:]))

	colors = ['#B20A2F', '#f55679', '#f8879f', '#780720']


	return [labels,data,colors]





def return_prediction_simple(df_cd, df_no):
	"""
	takes a dataframe with continuous/discrete values, and a dataframe with nominal/oridinal values
	and returns a prediction as a string.

	"""
	today = date.today()

	if int(df_cd.stm_reactie_duur.loc[0])< 480:

		df_no['weeknr'] = f"weeknr_w{today.isocalendar()[1]}"

		with open('webapp/text_files/dummies_mini.txt') as f:
			lines = f.readlines()

		all_dummies = [x.strip() for x in lines]

		dummie_df = pd.DataFrame({x: [0] for x in all_dummies})

		nom_vals = [df_no['weeknr'].loc[0], df_no['Oorzaak'].loc[0]]

		for x in nom_vals:
			dummie_df[x.strip()] = 1

		df = df_cd.join(dummie_df)

		print(list(df)[-1])
		filename = 'webapp/ml_algorithms/mini_decision_tree.sav'

		clf = pickle.load(open(filename, 'rb'))

		pred = clf.predict(df.values)[0]

		return (f'{0 + ((pred-1) * 5)} - {5 + ((pred-1) * 5)}'), get_graph_data(clf.predict_proba(df)[0])
	else:
		return '480+'


def return_prediction_reactie(df_cd, df_no):
	"""
	takes a dataframe with continuous/discrete values, and a dataframe with nominal/oridinal values
	and returns a prediction as a string.

	"""
	today = date.today()

	with open('webapp/text_files/dummies_reactie.txt') as f:
		lines = f.readlines()

		all_dummies = [x.strip() for x in lines]

		dummie_df = pd.DataFrame({x: [0] for x in all_dummies})

		nom_vals = [df_no['Traject'].loc[0],df_no['meldtijd_h'].loc[0].split(':')[0] ,df_no['stm_equipm_soort_mld'].loc[0],
					df_no['stm_techn_mld'].loc[0]]

		for x in nom_vals:

			dummie_df[x] = 1

		df = df_cd.join(dummie_df)
		print(list(df))

		filename = 'webapp/ml_algorithms/decision_tree_duration_bin_reactie.sav'

		clf = pickle.load(open(filename, 'rb'))
		pred = clf.predict(df.values)[0]

		print((np.mean([((pred-1) * 5),(5 + ((pred-1) * 5))])))
		return(int(np.mean([((pred-1) * 5),(5 + ((pred-1) * 5))])) , get_graph_data(clf.predict_proba(df)[0]))

#stm_reactie_duur = 200
#stm_prioriteit = 7
#stm_km_tot_mld = 50

#data = ['stm_prioriteit', 'stm_reactie_duur', 'stm_km_tot_mld']
#df_cd = pd.DataFrame(data={v: [eval(v)] for v in data})

#Oorzaak = 'Oorzaak_Levering nutsbedrijf: elek/gas/water/tel'

#data = ['Oorzaak']
#df_no = pd.DataFrame({v: [eval(v)] for v in data})
#
#
#print(return_prediction_simple(df_cd, df_no))

