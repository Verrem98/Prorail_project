from flask import Blueprint, render_template, request, jsonify
import pandas as pd
import csv
from webapp.prediction_generators import return_prediction_simple, return_prediction_reactie

views = Blueprint('views', __name__)


@views.route('/')
def herstel():
	contractgeb = []
	with open('webapp/text_files/contractgeb.txt', 'r') as cg1:
		reader = csv.reader(cg1)
		for row in reader:
			if len(row) > 1:
				c = row[0]
				contractgeb.append(c)

	# Contractgebied_
	oorzaak = []
	with open('webapp/text_files/oorzaak.txt', 'r') as o:
		reader = csv.reader(o)
		for row in reader:
			if len(row) > 1:
				c = row[0]
				oorzaak.append(c)
	return render_template(
		'index.html',
		oorzaak = oorzaak,
		contractgeb = contractgeb
	)


@views.route('/', methods = ['POST'])
def herstel_result():
	stm_reactie_duur = request.form['stm_reactie_duur']
	stm_prioriteit = request.form['stm_prioriteit']
	Oorzaak = request.form['Oorzaak']
	Contractgebied = request.form['Contractgebied']

	continu_df = pd.DataFrame(data = {'stm_reactie_duur': [stm_reactie_duur], 'stm_prioriteit': [stm_prioriteit]})

	dummies_df = pd.DataFrame(
		data = {'Oorzaak': [f"Oorzaak_{Oorzaak}"], 'Contractgebied': [f"Contractgebied_{Contractgebied}"]}
	)

	try:
		herstel, graphdata = return_prediction_simple(continu_df, dummies_df)
	except ValueError:
		herstel = return_prediction_simple(continu_df, dummies_df)
		return jsonify(hersteltijd = herstel, speling = '+- 20 min', graphdata = [None, None, None])

	return jsonify(hersteltijd = herstel, speling = '+- 20 min', graphdata = graphdata)


@views.route('/reactie')
def reactieduur():
	traject_options = []
	with open('webapp/text_files/traject.txt', 'r') as t:
		reader = csv.reader(t)
		for row in reader:
			if len(row) > 1:
				c = row[0]
				traject_options.append(c)

	techniek = {'S': 'Seinwezen',
				'B': 'Baan',
				'P': 'Post 21',
				'T': 'Telecom',
				'E': 'Energievoorziening',
				'K': 'Kunstwerken',
				'O': 'Operationeel beheer',
				'G': 'Gebouwen',
				'M': 'MR',
				'I': 'Ondergrondse infra',
				'X': 'Onbekend',
				'A': 'ATM'
				}

	oorzaak = []
	with open('webapp/text_files/oorzaak.txt', 'r') as o:
		reader = csv.reader(o)
		for row in reader:
			if len(row) > 1:
				c = row[0]
				oorzaak.append(c)

	soort_equipment = []
	with open('webapp/text_files/soort_equipment.txt', 'r') as se:
		reader = csv.reader(se)
		for row in reader:
			if len(row) > 1:
				c = row[0]
				soort_equipment.append(c)

	return render_template(
		'reactieduur.html',
		traject_options = traject_options,
		techniek = techniek, oorzaak = oorzaak,
		soort_equipment = soort_equipment,
	)


@views.route('/reactie', methods = ['POST'])
def reactie_duur_result():
	stm_km_tot_mld = request.form['stm_km_tot_mld']
	Traject = request.form['traject']
	meldtijd = request.form['meldtijd']
	stm_equipm_soort_mld = request.form['stm_equipm_soort_mld']
	stm_techn_mld = request.form['stm_techn_mld']

	print(stm_techn_mld)
	continu_df = pd.DataFrame(data = {'stm_km_tot_mld': [stm_km_tot_mld]})

	dummies_df = pd.DataFrame(
		data = {'Traject': [f"Traject_{Traject}"], 'meldtijd_h': [f"meldtijd_h_{meldtijd}"],
				'stm_equipm_soort_mld': [f"stm_equipm_soort_mld_{stm_equipm_soort_mld}"],
				'stm_techn_mld': [f"stm_techn_mld_{stm_techn_mld}"]}
	)

	duur, graphdata = return_prediction_reactie(continu_df, dummies_df)

	return jsonify(hersteltijd = duur, graphdata = graphdata)
