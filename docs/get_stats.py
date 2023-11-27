from SPARQLWrapper import SPARQLWrapper, JSON
import mysql.connector
from datetime import datetime

SUBJECTS_QRY = "SELECT ?_Label (COUNT(?item) AS ?count) WHERE {?item wdt:P5008 wd:Q100202113; wdt:P921 ?_ . SERVICE wikibase:label { bd:serviceParam wikibase:language 'en' . }} GROUP BY ?_ ?_Label HAVING (COUNT(?item) > 25) ORDER BY DESC (?count)"
SPARQL_USER_AGENT_ID = 'WikiframeApp/0.9 (https://github.com/aehulet; andre.hulet@unlv.edu)'
WIKIDATA_ENDPOINT = "https://query.wikidata.org/sparql"

def get_data(qry):
	spql = SPARQLWrapper(WIKIDATA_ENDPOINT, agent=SPARQL_USER_AGENT_ID)
	spql.setQuery(qry)
	spql.setReturnFormat(JSON)
	the_dict = spql.query()._convertJSON()

	return the_dict

def load_chart(the_dict):
	"""Used by get_data() to load source data into python list of objects."""
	results = []
	for r in the_dict["results"]["bindings"]:
		lab = str(r.get("_Label", {}).get("value"))
		cnt = int(r.get("count", {}).get("value"))		
		tup = (lab, cnt)		
		results.append(tup)		

	return results	

def get_creds():
	usr = ''
	pwd = ''
		
	with open('my.cnf', 'rt') as c:
		for l in c:
			if l[:4] == 'user':
				start = l.find("'") + 1
				end = l.find("'", start + 1)				
				usr = l[start:end]
			elif l[:4] == 'pass':
				start = l.find("'") + 1
				end = l.find("'", start + 1)				
				pwd = l[start:end]
		c.close()	

	return (usr, pwd)	

def write_log(msg):
	with open('scripting.log', 'a') as l:
		l.write(msg + '\n')
		l.close()

try:
	print("retrieving new subject report data from Wikidata...")
	dict1 = get_data(SUBJECTS_QRY)
	dat1_list = load_chart(dict1)

	creds = get_creds()	
	db = mysql.connector.connect(host="localhost", database="discover", user=creds[0], password=creds[1])	
	c = db.cursor()

	print('storing historical data and emptying report table...')
	
	c.callproc('cache_report_data')
	c.callproc('trunc_subject_data')	

	print("Loading new data into report table...")
	for r in dat1_list:	
		label = r[0]
		val = r[1]	
		c.callproc('insert_subject', (label, val))
	c.close()	
	print("Data caching complete.")
	write_log("{} Data successfully cached".format(datetime.now()))

except mysql.connector.Error as e:
	print(e)
	write_log("{} "+ str(e).format(datetime.now()))
	
	