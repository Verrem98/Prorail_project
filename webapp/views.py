from flask import Blueprint, render_template, request, json
import pandas

views = Blueprint('views', __name__)


@views.route('/')
def homepage():
	traject_options = [
		'Aachen (D) - Herzogenrath (D)',
		'Alkmaar',
		'Alkmaar - Uitgeest',
		'Almelo',
		'Almelo - Hengelo',
		'Almelo Dollegoor',
		'Almelo Gem. Stamlijn',
		'Alphen a/d Rijn',
		'Alphen a/d Rijn - Leiden Centraal',
		'Alphen a/d Rijn Industrieterrein Rijnhaven',
		'Amersfoort',
		'Amersfoort - Amersfoort Aansl.',
		'Amersfoort Aansl.',
		'Amersfoort Aansl. - Barneveld Noord',
		'Amersfoort Aansl. - Hattemerbroek',
		'Amersfoort Bokkeduinen',
		'Amersfoort Hoofdwerkplaats',
		'Amstelveen - Amsterdam Haarlemmermeer',
		'Amstelveen - Uithoorn',
		'Amsterdam - Vlissingen',
		'Amsterdam Bijlmer - Nieuwersluis-Loenen',
		'Amsterdam Bijlmer Arena',
		'Amsterdam Centraal',
		'Amsterdam Dijksgracht',
		'Amsterdam Hemhaven (gebied)',
		'Amsterdam Houtrakpolder (gebied)',
		'Amsterdam Lijnwerkplaats',
		'Amsterdam Muiderpoort',
		'Amsterdam Muiderpoort - Diemen',
		'Amsterdam Muiderpoort - Duivendrecht',
		'Amsterdam Riekerpolder',
		'Amsterdam Riekerpolder - Warmond',
		'Amsterdam Singelgracht Aansl.',
		'Amsterdam Sloterdijk',
		'Amsterdam Sloterdijk - Amsterdam Riekerpolder',
		'Amsterdam Sloterdijk - Haarlem',
		'Amsterdam Westhaven (gebied)',
		'Amsterdam Westhaven - Oldenzaal',
		'Apeldoorn',
		'Apeldoorn - Deventer',
		'Apeldoorn - Zutphen',
		'Arnhem',
		'Arnhem - Elst',
		'Arnhem - Velperbroek Aansl.',
		'Arnhem Gem. Stamlijn',
		'Arnhem Goederenstation - Velperbroek Aansl.',
		'Assen',
		'Assen - Haren',
		'Axel Axelse Vlakte',
		'Baarn',
		'Baarn - Amersfoort',
		'Barneveld Noord',
		'Barneveld Noord - Apeldoorn',
		'Barneveld Noord - Ede-Wageningen',
		'Beugen',
		'Beugen - Blerick',
		'Beverwijk Hoogovens - Roosendaal/Sloe',
		'Beverwijk Hoogovens - Zevenaar',
		'Beverwijk Hoogovens, Van Gelder',
		'Blauwkapel',
		'Blauwkapel - Den Dolder',
		'Blauwkapel - Lunetten',
		'Blerick',
		'Blerick - Eindhoven',
		'Born Franciscushaven',
		'Botlek',
		'Botlektunnel',
		'Boxtel',
		'Boxtel - Eindhoven',
		'Boxtel - Uden',
		'Breda',
		'Breda - Lage Zwaluwe',
		'Breda - Tilburg',
		'Breukelen',
		'Breukelen - Harmelen Aansl.',
		'Breukelen - Utrecht Centraal',
		'Budel Grens - Weert',
		'Budel Zinkfabriek',
		'CUP Valburg',
		'Coevorden - Coevorden Grens',
		'Coevorden Grens - Bentheim (D)',
		'Crailoo Bovenbouwwerkplaats',
		'De Haar Aansl.',
		'De Haar Aansl. - Ede-Wageningen',
		'Delden SERVO',
		'Delfzijl Stamlijn Havenschap',
		'Den Dolder',
		'Den Dolder - Amersfoort',
		'Den Dolder - Baarn',
		'Den Haag Binckhorst',
		'Den Haag Centraal',
		'Den Haag HS',
		'Den Haag HS - Schiedam Centrum',
		'Den Haag Laan van NOI',
		'Den Haag Mariahoeve',
		'Den Helder - Emmerich',
		'Den Helder - Heerhugowaard',
		'Deventer',
		'Deventer - Wierden',
		'Deventer - Zwolle',
		'Diemen',
		'Diemen - Duivendrecht',
		'Diemen Aansl.',
		'Diemen Aansl. - Weesp Aansl.',
		'Dieren',
		'Dieren - Apeldoorn',
		'Dieren - Zutphen',
		'Dordrecht',
		'Dordrecht - Rotterdam Barendrecht',
		'Dordrecht Industrieterrein Aansl. De Staart',
		'Dordrecht Zeehaventerrein',
		'Duivendrecht',
		'Duivendrecht - Amsterdam Riekerpolder',
		'Ede-Wageningen',
		'Ede-Wageningen - Arnhem',
		'Eijsden - Maastricht',
		'Eindhoven',
		'Eindhoven - Weert',
		'Elst',
		'Emmen - Weerdinge',
		'Emmen Emmtec',
		'Emmerich (D) - Zevenaar Grens',
		'Enschede - Amsterdam',
		'Enschede - Den Haag',
		'Enschede - Schiphol',
		'Etten-Leur Gem. Industrieterrein',
		'Geldermalsen',
		'Geldermalsen - Dordrecht',
		'Gent (B) - Zelzate (B)',
		'Gouda',
		'Gouda - Alphen a/d Rijn',
		'Gouda - Moordrecht Aansl.',
		'Gronau (D) - Enschede Grens',
		'Groningen',
		'Groningen - Drachten',
		'Groningen - Sauwerd',
		'Groningen Losplaats',
		'Groningen Losplaats - Waterhuizen Aansl.',
		'Groningen/Leeuwarden - Den Haag',
		'Groningen/Leeuwarden - Rotterdam',
		'Haarlem',
		'Haarlem - Santpoort Noord',
		'Haarlem - Warmond',
		'Haarlem - Zandvoort aan Zee',
		'Haarlem Goederenstation',
		'Haarlem Hoofdwerkplaats',
		'Haren',
		'Haren - Groningen Losplaats',
		'Haren - Waterhuizen Aansl.',
		'Harlingen Haven - Leeuwarden',
		'Harmelen Aansl.',
		'Harmelen Aansl. - Woerden',
		'Hattemerbroek',
		'Hazeldonk Grens - Noorderkempen (B)',
		'Heerenveen - Groningen',
		'Heerhugowaard',
		'Heerhugowaard - Alkmaar',
		'Heerhugowaard - Hoorn',
		'Heerlen',
		'Heerlen - Landgraaf',
		'Heerlen - Schin op Geul',
		'Hengelo',
		'Hengelo - Enschede Grens',
		'Hengelo - Hengelo Zoutindustrie',
		'Hengelo - Oldenzaal Grens',
		'Hengelo Akzo Zout Chemie',
		'Herfte Aansl.',
		'Herfte Aansl. - Mariënberg',
		'Herfte Aansl. - Meppel',
		'Herzogenrath (D)',
		'Hilversum',
		'Hilversum - Baarn',
		'Hilversum - Blauwkapel',
		'Hoorn',
		'Hoorn - Enkhuizen',
		'Hoorn - Medemblik',
		'Hulst Grens - Terneuzen Aansl.',
		'Kesteren - Geldermalsen',
		'Kijfhoek',
		'Kijfhoek - Lutterade DSM',
		'Kijfhoek - Meteren Aansl.',
		'Kijfhoek - Moerdijkbrug',
		'Kijfhoek - Oldenzaal',
		'Kijfhoek - Roosendaal/Sloe',
		'Kortsluitroute',
		'Lage Zwaluwe',
		'Lage Zwaluwe - Dordrecht',
		'Lage Zwaluwe - Roosendaal',
		'Lage Zwaluwe - s Hertogenbosch',
		'Lanaken (B) - Maastricht Grens',
		'Landgraaf',
		'Landgraaf - Haanrade Grens',
		'Landgraaf - Simpelveld',
		'Leeuwarden',
		'Leeuwarden - Groningen',
		'Leeuwarden - Stavoren',
		'Leiden Centraal',
		'Leiden Centraal - Den Haag Mariahoeve',
		'Leidschendam Lijnwerkplaats',
		'Lelystad Industrieterrein - Hattemerbroek',
		'Linne Grinderij',
		'Lunetten - De Haar Aansl.',
		'Lunetten - Geldermalsen',
		'Lunetten Aansl.',
		'Maastricht',
		'Maastricht - Maastricht Grens',
		'Maastricht - Sittard',
		'Maastricht Racc. Beatrixhaven',
		'Maasvlakte - Onnen',
		'Maasvlakte - Venlo',
		'Maasvlakte - Zevenaar',
		'Maasvlakte 2',
		'Mariënberg',
		'Mariënberg - Almelo',
		'Mariënberg - Emmen',
		'Meppel',
		'Meppel - Assen',
		'Meppel - Leeuwarden',
		'Meteren Aansl.',
		'Meteren Aansl. - Ressen-Bemmel',
		'Meteren Aansl. - s Hertogenbosch',
		'Moerdijk Industrieterrein',
		'Moordrecht Aansl.',
		'Moordrecht Aansl. - Den Haag Binckhorst',
		'Moordrecht Aansl. - Rotterdam Kleiweg',
		'Nederland',
		'Neerpelt (B) - Budel Grens',
		'Nieuw Amsterdam - Schoonebeek',
		'Nieuwersluis-Loenen',
		'Nieuwersluis-Loenen - Breukelen',
		'Nieuweschans Grens - Ihrhove (D)',
		'Nijmegen',
		'Nijmegen - Beugen',
		'Nijmegen Grens - Nijmegen',
		'Noordoost',
		'Nootdorp Aansl.',
		'Nootdorp Aansl. - Den Haag Laan van NOI',
		'Oldenzaal Grens - Bad Bentheim (D)',
		'Onnen Lijnwerkplaats',
		'Onnen Rangeerterrein',
		'Oosterhout Weststad',
		'Oss Racc. Elzenburg',
		'Pernis',
		'Prinsenbeek',
		'Prinsenbeek - Hazeldonk Grens',
		'Randstad Noord',
		'Randstad Zuid',
		'Ressen-Bemmel',
		'Ressen-Bemmel - Nijmegen',
		'Ressen-Bemmel - Zevenaar',
		'Rhenen - De Haar Aansl.',
		'Roermond',
		'Roermond - Venlo',
		'Roermond - Vlodrop Grens',
		'Roodeschool Eemshaven',
		'Roosendaal',
		'Roosendaal - Breda',
		'Roosendaal - Oldenzaal',
		'Roosendaal - Roosendaal Grens',
		'Roosendaal - Vlissingen',
		'Roosendaal Borchwerf',
		'Roosendaal Grens - Essen (B)',
		'Roosendaal Industrieterrein',
		'Rotterdam - Venlo',
		'Rotterdam Barendrecht',
		'Rotterdam Centraal',
		'Rotterdam Eemhaven',
		'Rotterdam Europoort 1',
		'Rotterdam Europoort 2',
		'Rotterdam Europoort 3',
		'Rotterdam Europoort 4',
		'Rotterdam Kleiweg',
		'Rotterdam Kleiweg - Nootdorp Aansl.',
		'Rotterdam Kleiweg - Rotterdam Westelijke Splitsing',
		'Rotterdam Lombardijen',
		'Rotterdam Lombardijen - Rotterdam Centraal',
		'Rotterdam Maasvlakte',
		'Rotterdam Rijn- en Maashaven',
		'Rotterdam Waalhaven Oost',
		'Rotterdam Westelijke Splitsing',
		'Rotterdam Westelijke Splitsing - Nieuw Vennep',
		'Rotterdam Zuid Goederen - Rotterdam Maasvlakte',
		'Santpoort Noord',
		'Santpoort Noord - IJmuiden',
		'Santpoort Noord - Uitgeest',
		'Sas van Gent Cerestar',
		'Sas van Gent Grens - Terneuzen Aansl.',
		'Sauwerd',
		'Sauwerd - Delfzijl',
		'Sauwerd - Winsum',
		'Schiedam Centrum',
		'Schiedam Centrum - Hoek van Holland Strand',
		'Schin op Geul',
		'Schin op Geul - Maastricht',
		'Simpelveld',
		'Simpelveld - Schin op Geul',
		'Simpelveld Grens - Simpelveld',
		'Sittard',
		'Sittard - Born',
		'Sittard - Heerlen',
		'Sittard - Roermond',
		'Sloe - Venlo',
		'Stadskanaal Hoofdstation - Musselkanaal-Valthermond',
		'Stadskanaal Hoofdstation - Zuidbroek',
		'Terneuzen Aansl.',
		'Terneuzen Aansl. - Terneuzen',
		'Terneuzen Dow Chemical',
		'Tiel Gem. Stamlijn',
		'Tilburg',
		'Tilburg - Boxtel',
		'Tilburg - Vught Aansl.',
		'Tilburg Hoofdwerkplaats',
		'Tilburg de Loven',
		'Uitgeest',
		'Uitgeest - Zaandam',
		'Uitgeest/Haarlem - Zevenaar',
		'Utrecht - Heerlen/Maastricht',
		'Utrecht Centraal',
		'Utrecht Centraal - Blauwkapel',
		'Utrecht Centraal - Harmelen Aansl.',
		'Utrecht Industrieterrein Lage Weide',
		'VAM-terrein Wijster',
		'Velperbroek Aansl.',
		'Velperbroek Aansl. - Dieren',
		'Velperbroek Aansl. - Zevenaar',
		'Venlo',
		'Venlo -Lutterade DSM',
		'Venlo Grens - Keulen (D)',
		'Venlo Grens - Venlo',
		'Venlo Tradeport',
		'Vetschau (D) - Simpelveld Grens',
		'Visé (B) - Eijsden Grens',
		'Vlissingen Sloehaven',
		'Vork',
		'Vork - Kesteren',
		'Vught Aansl.',
		'Vught Aansl. - Boxtel',
		'Warmond',
		'Warmond - Leiden Centraal',
		'Watergraafsmeer',
		'Waterhuizen Aansl.',
		'Waterhuizen Aansl. - Zuidbroek',
		'Weert',
		'Weert - Roermond',
		'Weesp Aansl.',
		'Weesp Aansl. - Hilversum',
		'Weesp Aansl. - Lelystad Industrieterrein',
		'Wierden',
		'Wierden - Almelo',
		'Winsum - Roodeschool',
		'Winterswijk',
		'Winterswijk - Zevenaar',
		'Woerden',
		'Woerden - Alphen a/d Rijn',
		'Woerden - Gouda',
		'Woudenberg-Scherpenzeel - Amersfoort',
		'Zaandam',
		'Zaandam - Amsterdam Singelgracht Aansl.',
		'Zaandam - Amsterdam Sloterdijk',
		'Zaandam - Hoorn',
		'Zelzate (B) - Sas van Gent Grens',
		'Zevenaar',
		'Zevenaar - Zevenaar Grens',
		'Zuid',
		'Zuidbroek',
		'Zuidbroek - Nieuweschans Grens',
		'Zutphen',
		'Zutphen - Deventer',
		'Zutphen - Hengelo',
		'Zutphen - Winterswijk',
		'Zwijndrecht Groote Lindt',
		'Zwolle',
		'Zwolle - Herfte Aansl.',
		'Zwolle - Kampen',
		'Zwolle - Roosendaal',
		'Zwolle - Wierden',
		'Zwolle Industrieterrein Katwolde',
		'Zwolle Lijnwerkplaats',
		'Zwolle Rangeerterrein',
		's Hertogenbosch',
		's Hertogenbosch - Nijmegen',
		's Hertogenbosch - Vught Aansl.',
		's Hertogenbosch Gem. Stamlijn'
	]

	techniek = {
		'S': 'Seinwezen',
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

	oorzaak = [
		'Aanrijding (bijna) tijdens werkzaamheden',
		'Aanrijding met personen langs de baan',
		'Aanrijding met wegverkeer',
		'Afstelling onjuist/verlopen',
		'Applicatie/softwarefout',
		'Belemmerende vegetatie',
		'Bij onderzoek in orde/geen oorzaak gevonden',
		'Bijna aanrijding met persoon langs baan',
		'Bijna aanrijding met wegverkeer',
		'Braamvorming',
		'Brand(alarm), bommelding, gevaar/explosie',
		'Breuk/scheurvorming/afbrokkeling',
		'Corrosie/aantasting',
		'Defect bijzonder voertuig tijdens transport',
		'Diefstal',
		'Dieren, schade door of (bijna) aanrijding',
		'Doorbranden',
		'EMC/bliksem',
		'Extreem hoge temperatuur',
		'Extreem lage temperatuur',
		'Fabricagefout',
		'Geen onderzoek',
		'Gladde sporen (bladval/chemicalien)',
		'Golfslijtage',
		'Groefvorming',
		'IJsafzetting/ijzel',
		'In- en uitzetten materieel',
		'Ingebrand/verbrand',
		'Inrijden',
		'Isolatie',
		'Katterug',
		'Klapper',
		'Kortsluiten',
		'Lekkage',
		'Levering nutsbedrijf: elek/gas/water/tel',
		'Montagefout',
		'Niet gemeld',
		'Omhoog werken/verschuiven',
		'Onderdeel defect door onbekende oorzaak',
		'Ondeskundig gebruik derden (bediening)',
		'Ongepland werk',
		'Onjuiste geometrie/ligging/blinde vering',
		'Onvoldoende onderhoud',
		'Onvoldoende smering',
		'Openrijden/kapotrijden',
		'Overbelasting',
		'Overig derden',
		'Overig processen',
		'Overig technisch',
		'Overspanning',
		'Pekel/zout',
		'RCF (headcheck)',
		'Regen/vocht/wateroverlast',
		'Schade door weg-/werk-/waterverkeer',
		'Slijtage',
		'Sneeuw/hagel',
		'Storm',
		'Systeemfout',
		'Trillingen',
		'Uitloop treinvrije periode',
		'Uitwalsing',
		'Vandalisme',
		'Vastgelopen',
		'Verbogen/vervormd',
		'Veroudering',
		'Verrot',
		'Vervuiling (derden)',
		'Vervuiling (technisch)',
		'Verzakking/klink/zetting',
		'Vreemd voorwerp',
		'Werkzaamheden',
	]

	soort_equipment = [
		'25AARDELEC',
		'25AARDVERB',
		'25AFNAMEPT',
		'25AFSPANN',
		'25AUTOTRAF',
		'25BESCHAAR',
		'25BEVEILHS',
		'25BOVNLEID',
		'25BVLSCHAK',
		'25CNTBDRVR',
		'25C_BANK',
		'25DRGCIE',
		'25DRGCIEBV',
		'25DRGKABEL',
		'25ELVERB',
		'25EQUIPOT',
		'25FASESCH',
		'25FILTER',
		'25HANGDR',
		'25HS_INSTA',
		'25ISOLATOR',
		'25KABEL_EV',
		'25LBDV',
		'25LEIDOND',
		'25LSTSCHAK',
		'25LSTSCHEI',
		'25LSVOED',
		'25MEETINSP',
		'25MVI',
		'25NEGAFEED',
		'25NOODSTRM',
		'25OVERSPAF',
		'25PRIMINST',
		'25RAILSPL',
		'25RETLAAR',
		'25RIJDRAAD',
		'25SCHAARDC',
		'25SECINSTA',
		'25SPANSLIN',
		'25STATTRAF',
		'25STROOMRL',
		'25TRACTRAF',
		'25VASTPUNT',
		'25VERMSCHA',
		'25ZIJWBEV',
		'25ZINKERK',
		'3BSAFNPUNT',
		'3KVAFNPUNT',
		'3KVKABEL',
		'3KVKABELSY',
		'3KVLASTSCH',
		'3KVLOCVOED',
		'3KVOMVCENT',
		'3KVTRAFOGR',
		'3KVVERDNET',
		'3KVVOEDPNT',
		'AARDELECT',
		'AARDELECTR',
		'AARDFTDET',
		'AARDSCHAK',
		'ACUUNIT',
		'AFNAMEPTHS',
		'AFNAMEPTLS',
		'AFSCHERM',
		'AFSPANNING',
		'AFSTBEDIEN',
		'AFST_STUUR',
		'ANTI_ICING',
		'AO1500VK',
		'AO1500VKAB',
		'AQUADUCT',
		'ARMATUUR',
		'ASSTELPNT',
		'ATBNGBAKEN',
		'ATBNGENC',
		'ATBNGLUS',
		'ATBVV',
		'ATBVVUNIT',
		'AUTOMDEUR',
		'BAANLICHAA',
		'BAANVRZIEN',
		'BALLAST',
		'BATTERIJ',
		'BBINSTALL',
		'BEHUIZBEV',
		'BESCH_AARD',
		'BEVTRACTGR',
		'BEVVK10-25',
		'BEVVK10_25',
		'BEVVOEDSEC',
		'BEV_EV',
		'BEV_KABEL',
		'BEWEEGBARM',
		'BEWWERK',
		'BIJZCONSTR',
		'BIJZNSTSPR',
		'BLUSAFNHYD',
		'BLUSVULHYD',
		'BLUSWVOORZ',
		'BOVENLEID',
		'BRUGBED',
		'BRUGBEVAPP',
		'BRUGOVERG',
		'BRWSLKLUIS',
		'BVLAFSCHER',
		'BVLSCHAK',
		'CABHP',
		'CABOP',
		'CAMERA',
		'CCTV_CAM',
		'CCTV_STOR',
		'CCTV_UITK',
		'CISJRELAIS',
		'CNTR_BDRVR',
		'COMPENSINR',
		'COMPLAS',
		'COMPLEX',
		'C_BANK',
		'DCBUS',
		'DEPOTVOED',
		'DETASSAZA',
		'DETASSBATT',
		'DETASSEAK',
		'DETASSFWS',
		'DETASSTLPT',
		'DETASSUNIT',
		'DETASSVOED',
		'DETEBIEVAL',
		'DETECTREIN',
		'DETFTGSSEC',
		'DETGRSSSL',
		'DETJAD2COM',
		'DETJADE1SL',
		'DETJADE2SL',
		'DETJADPOW',
		'DETLUS',
		'DETOTCSSL',
		'DETPEDAAL',
		'DETPSSSL',
		'DIJKCOUPUR',
		'DILATINR',
		'DIVDOORSN',
		'DRAAGKABEL',
		'DRAINAGE',
		'DRAINAGEZW',
		'DRGCIE',
		'DRGCIEBVL',
		'DUIKER',
		'EBSBATT',
		'EBSEXINTEQ',
		'EBSINTFMOD',
		'EBSRECHNER',
		'EBSSUPPCOM',
		'EBSSUPPEQ',
		'EBSWRECHNR',
		'EBSWSUPCOM',
		'EBSWSUPEQ',
		'ECODUCT',
		'ELECGREN',
		'ELECTVERB',
		'EMPLVOORZ',
		'ESLAS',
		'ETCSACCSER',
		'ETCSALIS',
		'ETCSBALISE',
		'ETCSLEU',
		'ETCSRBC',
		'ETCSSERVER',
		'FAUNAVRZ',
		'FECAAFVOER',
		'FIDES',
		'FIETSENVZ',
		'FLYOVER',
		'FRAME',
		'FREQOMVORM',
		'FUNDERING',
		'GAASAFSCH',
		'GASBEWKAST',
		'GEBOUW',
		'GEBOUWBEV',
		'GEB_GBINST',
		'GELIJKR',
		'GELIJKSPIN',
		'GELUIDSSCH',
		'GENATMNET',
		'GESPREKREG',
		'GLASVEZEL',
		'GOEDVOORZ',
		'GROEPSKAST',
		'GSMR',
		'GVI',
		'GVIGESTELA',
		'GVI_ONDERD',
		'HAAG',
		'HANGDRAAD',
		'HEKWERK',
		'HELLINGBAA',
		'HEUVELBEST',
		'HEUVELSYS',
		'HFREQINS',
		'HOOGSPINST',
		'HOTBOXDET',
		'HVI',
		'HVIAARDING',
		'HYDRAULIEK',
		'ICTINFRA',
		'ICTSOFTW',
		'INFRASTR',
		'INSPECTWGN',
		'INTERCOM',
		'INTERLOCK',
		'INTLOCKUNT',
		'INUITVOORZ',
		'ISOLATOR',
		'KABEL10_25',
		'KABEL1500V',
		'KABELBED',
		'KABELKAST',
		'KABELTRGP',
		'KABEL_EV',
		'KABLEIDKOK',
		'KAP',
		'KBL1500VMI',
		'KIJFDIS',
		'KOPERKABEL',
		'KROKODIL',
		'KRUISING',
		'KRUISSTUK',
		'LASTSCHAK',
		'LASTSCHEID',
		'LBDV',
		'LEIDINGEN',
		'LEIDINGOND',
		'LIFT',
		'LIFTEN',
		'LOC_VOED',
		'LSVERDINR',
		'LUIDSPR',
		'LVAARDELEC',
		'LVDSVERDIN',
		'LVHSKABEL',
		'LVHSTRAFO',
		'LVHVI',
		'LVI',
		'LVNOODSTAG',
		'LVNOODSTGR',
		'MARIFOON',
		'MECHOVERBR',
		'MINUSKAST',
		'MOBCOMSYST',
		'MODULE',
		'MONITMATRL',
		'MONITOR',
		'NBSTATION',
		'NOODAFSL',
		'NSA',
		'NSPSPBORD',
		'NTSPRDRGKW',
		'NUTSELEKTR',
		'NUTSGAS',
		'NUTSWATER',
		'OMROEPHP',
		'OMROEPOP',
		'ONDERDGANG',
		'ONDERSTAT',
		'ONTSPBED',
		'ONTSPINR',
		'OVERGCONST',
		'OVERWBEVL',
		'OVERWEG',
		'OVRSPBBVL',
		'OVWBATT',
		'OVWBESTUR',
		'OVWBEV',
		'OVWGELYKR',
		'OVWGLICHT',
		'OVWPAAL',
		'OVWSTELLER',
		'PERRNBESCH',
		'PERRON',
		'PERRONGEB',
		'PERRONKAP',
		'PERRONVRZ',
		'PERSLUCHT',
		'PLAATSBEP',
		'PLCSUPPEQ',
		'PLTSBEDAPP',
		'POORT',
		'PORTOFOON',
		'PSV',
		'PUNTSTUK',
		'QUOVADIS',
		'RAILDEMPER',
		'RAILGEBOUW',
		'REEDSTUUR',
		'REISINF',
		'RELAIS',
		'RELAISB1',
		'RELAISB2',
		'RELAISCT',
		'RELAISTIJD',
		'RELAISVTB',
		'REMBEPINST',
		'REMBEPRKST',
		'REMPRINST',
		'RETA1500V',
		'RETOURLEID',
		'RIJDRAAD',
		'RIJWIELST',
		'RISANALOOG',
		'RISDIGITAL',
		'ROLTRAPPEN',
		'RUIMTE',
		'SCHAKELST',
		'SECUND_INS',
		'SEIN',
		'SEINBRUG',
		'SEINLAMPH',
		'SEINLED',
		'SEINMSG',
		'SEIN_BORD',
		'SERVER',
		'SERVPUNT',
		'SERVRNGPER',
		'SLOTEN',
		'SMEERINR',
		'SMLCLCCOM',
		'SMLSERVER',
		'SMLSUPPEQ',
		'SMLTFMCOM',
		'SNSCHAKAUT',
		'SOFTWARE',
		'SPANSLUIS',
		'SPDVBSCHAK',
		'SPOORBEGR',
		'SPOORBEV',
		'SPOORBRUG',
		'SPOORCONST',
		'SPOORDRKW',
		'SPOORDWL',
		'SPOORSPS',
		'SPOORSTUK',
		'SPOORTAK',
		'SPOORTOEST',
		'SPOORTUN',
		'SPRAAKCOM',
		'SPRVIADUCT',
		'SSCSKAST',
		'SSCSKOP',
		'STABCONSTR',
		'STATION',
		'STATIONGEB',
		'STATIONHAL',
		'STATIONTUN',
		'STATOMROEP',
		'STATOUTILL',
		'STATTRAFO',
		'STORSIGDEC',
		'STORSIGN',
		'STRAHERSTS',
		'STRKREGEL',
		'STROOMRAIL',
		'SYSTBOVENL',
		'TALUDTRAP',
		'TANKINST',
		'TANKVOORZ',
		'TBHHARDW',
		'TECHNRUIM',
		'TECINSTGEB',
		'TELCENTRAL',
		'TELECOMKBL',
		'TELEFOONS',
		'TERREIN',
		'TERREININR',
		'TERREINVL',
		'TIJDCOM',
		'TIJDHP/OP',
		'TIJDKLOK',
		'TIJDONTVAN',
		'TOEGANG',
		'TOEGANGBEV',
		'TOEGANGPRT',
		'TOEGANGSVZ',
		'TOEGTRANVZ',
		'TONGBEW',
		'TONGCONTR',
		'TRAFO',
		'TRAFOGR',
		'TRANSMISSI',
		'TREINBEINV',
		'TREINVOORV',
		'TRGELIJKR',
		'TRGROEP',
		'TRTRAFO',
		'TTI',
		'TUNCONSTR',
		'UPS',
		'UPSTBP21TE',
		'VASTETRAP',
		'VASTGOED_R',
		'VASTPUNT',
		'VERBINDOBJ',
		'VERGRENDEL',
		'VERHARDING',
		'VERKBRGVIA',
		'VERLTRANSF',
		'VERVALKW',
		'VIDEOCOMMU',
		'VISUELERIS',
		'VOEDBEWAK',
		'VOEDING',
		'VOEDINGSOV',
		'VOEDKAST',
		'VPIEXINTEQ',
		'VPIMODULE',
		'VPISUPPCOM',
		'VPISUPPEQ',
		'V_LEIDING',
		'WACHSTATGB',
		'WASMBVL',
		'WASVULHYDR',
		'WATERAANSL',
		'WATERVPUNT',
		'WEERSTAT',
		'WERKPLBBED',
		'WERKPLBEV',
		'WERKPLBSIG',
		'WERKPLHHT',
		'WINDVAAN',
		'WISSBEDIEN',
		'WISSCONS',
		'WISSEL',
		'WISSELSTEL',
		'WISSMOTOR',
		'WISVERWINS',
		'WVKAST',
		'Y_DRAAD',
		'ZETVRPLAAT',
		'ZIJWBEV',
		'ZINKERKAST',
		'ZMX',
	]

	contractgeb = [
		0.0,
		1.0,
		2.0,
		3.0,
		4.0,
		5.0,
		6.0,
		7.0,
		8.0,
		9.0,
		10.0,
		11.0,
		12.0,
		13.0,
		14.0,
		15.0,
		16.0,
		17.0,
		18.0,
		19.0,
		20.0,
		21.0,
		22.0,
		23.0,
		24.0,
		25.0,
		26.0,
		27.0,
		28.0,
		29.0,
		30.0,
		31.0,
		32.0,
		33.0,
		34.0,
		35.0,
		36.0,
		37.0,
		50.0,
		51.0,
		52.0,
		53.0,
		54.0,
		55.0,
		56.0,
		57.0,
		58.0,
		59.0,
		60.0,
		61.0,
		62.0,
		63.0,
		64.0,
		70.0,
		71.0,
		81.0,
		82.0,
		83.0,
		99.0
	]

	return render_template(
		'index.html',
		traject_options = traject_options,
		techniek = techniek, oorzaak = oorzaak,
		soort_equipment = soort_equipment,
		contractgeb = contractgeb
	)


@views.route('/', methods = ['POST'])
def result():
	stm_km_tot_mld = request.form['stm_km_tot_mld']
	stm_km_van_mld = request.form['stm_km_van_mld']
	smt_reactie_duur = request.form['smt_reactie_duur']
	meldtijd = request.form['meldtijd']
	stm_techn_mld = request.form['stm_techn_mld']
	stm_prioriteit = request.form['stm_prioriteit']
	Oorzaak = request.form['Oorzaak']
	stm_equipm_soort_mld = request.form['stm_equipm_soort_mld']
	Traject = request.form['traject']
	stm_contractgeb_gst = request.form['stm_contractgeb_gst']

	continu_df = pandas.DataFrame(data={'stm_km_tot_mld': [stm_km_tot_mld], 'stm_km_van_mld': [stm_km_van_mld], 'smt_reactie_duur': [smt_reactie_duur], 'stm_prioriteit': [stm_prioriteit]})

	dummies_df = pandas.DataFrame(data={'Traject': [Traject], 'meldtijd': [meldtijd], 'stm_equipm_soort_mld': [stm_equipm_soort_mld], 'stm_techn_mld': [stm_techn_mld], 'Oorzaak': [Oorzaak], 'stm_contractgeb_gst': [stm_contractgeb_gst]})

	return json.dumps({'prediction': 'Check', 'stm_km_tot_mld': stm_km_tot_mld, 'stm_km_van_mld': stm_km_van_mld})
