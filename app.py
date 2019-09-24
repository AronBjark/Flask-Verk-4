from flask import Flask, render_template as rend

app = Flask(__name__)

lorem_ipsum = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Lorem mollis aliquam ut porttitor leo a. Pellentesque eu tincidunt tortor aliquam nulla facilisi cras fermentum. Nisl nunc mi ipsum faucibus vitae aliquet. Ultricies lacus sed turpis tincidunt id aliquet risus feugiat. Arcu ac tortor dignissim convallis aenean et tortor. Aliquam vestibulum morbi blandit cursus risus at. Feugiat in ante metus dictum at tempor commodo ullamcorper. Magnis dis parturient montes nascetur ridiculus mus. Sed libero enim sed faucibus turpis in eu. Sed tempus urna et pharetra. Tincidunt vitae semper quis lectus nulla at. Blandit massa enim nec dui nunc mattis enim. Amet commodo nulla facilisi nullam. Pulvinar elementum integer enim neque volutpat ac tincidunt vitae semper. Sodales ut eu sem integer. Viverra suspendisse potenti nullam ac tortor vitae purus.'

articles = [{'id': 1, 'author': "Siggi litli", 'title': "3 af hverjum 5 drengjum kunna ekki að tala", 'content': lorem_ipsum},
			{'id': 2, 'author': "Jói Fel", 'title': "Hamborgarar valda lifrabólgu", 'content': lorem_ipsum},
			{'id': 3, 'author': "Raggi Bjarna", 'title': "Epla ormar eru ekki við hæfi barna", 'content': lorem_ipsum}]

people = [{'name': "Helga.", 'kt': "1234564321"},
		  {'name': "Hulda.", 'kt': "4568985245"},
		  {'name': "Bogga.", 'kt': "6548972583"}]

lenA, lenB = len(articles), len(people)

@app.route('/')
def index():
	return '<h1>Velkominn</h1><a href="/article/1">Fréttaverkefni</a> | <a href="/kennitala/1234564321">kennitölu Verkefni</a>'

@app.route('/article/<ID>')
def article(ID):
	for x in range(lenA):
		if int(ID) == articles[x]['id']:
			d = articles[x]
			a, t, c = d['author'], d['title'], d['content']
	return rend('layout.html', author=a, title=t, content=c, articles=articles, len=lenA)

@app.route('/kennitala/<KT>')
def kennitala(KT):
	for x in range(lenB):
		if KT == people[x]['kt']:
			p = people[x]
			n, k, s = p['name'], p['kt'], 0
			for x in KT: s += int(x)
	return rend('kennitala.html', name=n, kt=k, people=people, len=lenB, sum=s)




@app.errorhandler(404)
def error404(error):
	return '<br><br><h1 style="text-align: center;">Villa 404</h1><h2 style="text-align: center;">Þessi síða er ekki til<h2>'
if __name__ == "__main__":
	app.run(debug=True)