import pandas as pd
import pickle
from datetime import date


def get_graph_data(prob_list):


	prob_dict = {(i+1): prob_list[i] for i in range(len(prob_list))}
	prob_dict = {k: v for k, v in sorted(prob_dict.items(), key=lambda item: item[1], reverse=True)}



	labels = list([f'{0 + ((i-1) * 5)} - {5 + ((i-1) * 5)} min' for i in prob_dict.keys()])[:3]
	labels.append('Overig')

	data = list(prob_dict.values())[:3]
	data.append(sum(list(prob_dict.values())[3:]))

	colors = ['#B20A2F', '#f55679', '#f8879f', '#780720']


	return [labels,data,colors]





def return_prediction_simple(df_cd, df_no):
	today = date.today()

	if int(df_cd.stm_reactie_duur.loc[0])< 480:

		df_no['weeknr'] = f"weeknr_w{today.isocalendar()[1]}"

		with open('webapp/text_files/dummies.txt') as f:
			lines = f.readlines()

		all_dummies = [x.strip() for x in lines]

		dummie_df = pd.DataFrame({x: [0] for x in all_dummies})

		nom_vals = [df_no['weeknr'].loc[0], df_no['Oorzaak'].loc[0]]

		for x in nom_vals:
			dummie_df[x] = 1

		df = df_cd.join(dummie_df)

		filename = 'webapp/ml_algorithms/mini_decision_tree.sav'

		clf = pickle.load(open(filename, 'rb'))

		pred = clf.predict(df.values)[0]

		return (f'{0 + ((pred-1) * 5)} - {5 + ((pred-1) * 5)}'), get_graph_data(clf.predict_proba(df)[0])
	else:
		return '480+'

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

