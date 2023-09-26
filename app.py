from flask import Flask

app = Flask(__name__)


@app.route('/')

def hello_world():

 orang = {'nama': 'albardani', 'umur':'21thn'}

 komentar = [

  {

   'penulis': {'nama': 'Khalid'},

   'ucapan': 'hai albardani, artikel yang bagus'

  },

  {

   'penulis': {'nama': 'Ariqa'},

   'ucapan': 'artikel ini cukup membantu saya'

  }

 ]

 return render_template('index.html', title='Beranda', orang=orang, komentar=komentar)

<html>

    <head>

       {% if title %}

        <title>{{ title }} - Flask Blog</title>

        {% else %}

        <title>Selamat Datang - Flask Blog</title>

        {% endif %}

    </head>

    <body>

        <h1>Hello {{ orang.nama }}, Umur Anda {{ orang.umur }}!</h1>

    </body>

</html>'''