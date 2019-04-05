#coding: utf-8

from horoscope import generate_prophecies
from datetime import datetime as dt

def generate_page(head, body):
	page = f"<html>{head}{body}</html>"
	return page

def generate_head(title):
	head = f"""<head>
	<meta charset='utf-8'>
	<title>{title}</title>
	</head>
	"""
	return head

def generate_body(header, paragraphs):
	body = f"<h1>{header}</h1>"
	for p in paragraphs:
		body = body + f"<p>{p}</p>"
	return f"""<body>{body}<br><hr/><br><a href="about.html">О реализации</a></body>"""

def save_about(output="about.html"):
	fp = open(output, "w", encoding='utf-8')
	head = f"""<head>
	<meta charset='utf-8'>
	<title>"О чем все это"</title>
	</head>
	"""
	body = f"""<body>
	<img src="horoscope.jpg"/>
	<h2>Параметры генерации:</h2>
	<ol>
		<li>Времена дня:
			<ul>
				<li>Утром.</li>
				<li>Вечером.</li>
				<li>После обеда.</li>
			</ul>
        </li>
		<li>Глаголы:
			<ul>
				<li>ожидайте</li>
				<li>предостерегайтесь</li>
				<li>будьте открыты для</li>
			</ul>
		</li>
		<li>Ожидания:
			<ul>
				<li>гостей из забытого прошлого</li>
				<li>встреч со старыми знакомыми</li>
				<li>неожиданного праздника</li>
				<li>приятных перемен</li>
			</ul>
		</li>
	</ol>
	<br>
	<a href="index.html">Назад</a>
	</body>
	"""
	page = f"<html>{head}{body}</html>"
	print(page, file=fp)
	fp.close()

def save_page(title, header, paragraphs, output="index.html"):
	fp = open(output, "w", encoding='utf-8')
	today = dt.now().date()
	page = generate_page(
		head=generate_head(title),
		body=generate_body(header=header, paragraphs=paragraphs)
	)
	print(page, file=fp)
	fp.close()


#####################

today = dt.now().date()

save_about()

save_page(
	title="Гороскоп на сегодня",
	header="Ваши предсказания на " + str(today),
	paragraphs=generate_prophecies(3,4),
)