# -*- coding : iso-8859-15 -*-
from bottle import route, error, post, get, run, static_file, abort, redirect, response, request, template
import pymysql
import settings

alpha_key=list()
num=int()

@route('/presentation_of_artists')
def search_for_artists():
    return '''
<style type="text/css">
	p0 {
		padding-left: 39.5%;
	}
	p1 {
		padding-left: 35%;
	}
	p2 {
		padding-left: 6.45%;
	}
	p3 {
		padding-left: 5%;
	}
	p4 {
		padding-left: 0.55%;
	}
	p5 {
		padding-left: 1.95%;
	}
	p6 {
		padding-left: 2.5%;
	}
	p7 {
		padding-left: 3.6%;
	}
	p8 {
		padding-left: 34%;
	}

	h1 {
		font-size: 2em;
	}
</style>

<form align="left" accept-charset="UTF-8" method="post">
	<h1><p8><strong>&bull; Presentation of Artists</strong></p8></h1>
	<hr>
	<p1>Name<p2><input type="text" name="firstname"><br></p2></p1>
	<p1>Surname<p3><input type="text" name="lastname"><br></p3></p1>
	<p1>Birth Year - From<p4><input type="text" name="birthfrom"><br></p4></p1>
	<p1>Birth Year - To<p5><input type="text" name="birthto"><br></p5></p1>
	<p1><p2><p6><input type="radio" name="occupation" value="tragoudistis">Singer<br></p6></p2></p1>
	<p1>Type<p2><input type="radio" name="occupation" value="stixourgos">Song Writer<br></p2></p1>
	<p1><p2><p6><input type="radio" name="occupation" value="sinthetis">Composer</p6></p2></p1><br>
	<p0><p7><input type="submit" value="Submit"></p7></p0>
	<hr>
</form>
'''

@route('/presentation_of_artists', method='POST')
def get_artist():
    conn=pymysql.connect(
        settings.mysql_host,
        settings.mysql_user,
        settings.mysql_passwd,
        settings.mysql_schema,
        charset='utf8')

    cur=conn.cursor()
    a1=request.forms.get('firstname')
    a2=request.forms.get('lastname')
    a3=request.forms.get('birthfrom')
    a4=request.forms.get('birthto')
    a5=request.forms.get('occupation')

    s1=' AND onoma="%s" '
    s2=' AND epitheto="%s" '
    s3=' AND etos_gen>=%s '
    s4=' AND etos_gen<=%s '
    s5=' AND ar_taut IN (SELECT %s FROM singer_prod INNER JOIN (SELECT * from tragoudi)AS A ON title=titlos) '

    tup=(a1,a2,a3,a4,a5)
    
    if a1=='':
        s1='%s'
    if a2=='':
        s2='%s'
    if a3=='':
        s3='%s'
    if a4=='':
        s4='%s'
    if a5==None:
        s5='%s'
        tup=(a1,a2,a3,a4,'')

    stmt='SELECT * FROM kalitexnis WHERE 1=1'+s1+s2+s3+s4+s5
    cur.execute(stmt % tup)
    test_tuple=cur.fetchall()
    
    cur.close()
    conn.close()

    return template('temp.tpl', result = test_tuple)

@route('/')
def homepage():
    return '''
<hr>
<form align="center" action="/presentation_of_artists">
	<input type="submit" value="Update & Search Artists" style="width: 200px">
	<br>
</form>
<form align="center" action="/presentation_of_songs">
	<input type="submit" value="Search Songs" style="width: 200px">
	<br>
</form>
<form align="center" action="/insert_artists">
	<input type="submit" value="Insert Artists" style="width: 200px">
	<br>
</form>
<form align="center" action="/insert_songs">
	<input type="submit" value="Insert Song" style="width: 200px">
</form>
<hr>
'''

@route('/presentation_of_artists/update/<idnt>/<name>/<surname>/<year>')
def show_update_artist(idnt,name,surname,year):
    tup=(name,surname,year)
    return ('''
<style>
  h1 {
    font-size: 2em;
  }
</style>

<form accept-charset="UTF-8" method="post">
  <h1><strong>&bull; Update Artist Information</strong></h1>
  <hr>
  Name<input type="text" name="firstname" value="%s"><br>
  Surname<input type="text" name="lastname" value="%s"><br>
  Birth Year<input type="text" name="birthyear" value=%s><br>
  <input type="submit" value="Update Information">
  <hr>
</form>
''' % tup)

@route('/presentation_of_artists/update/<idnt>/<name>/<surname>/<year>', method='POST')
def update_artist(idnt):
    conn=pymysql.connect(
        settings.mysql_host,
        settings.mysql_user,
        settings.mysql_passwd,
        settings.mysql_schema,
        charset='utf8')

    cur=conn.cursor()

    tup=(request.forms.get('firstname'),request.forms.get('lastname'),request.forms.get('birthyear'),idnt)
    
    cur.execute('UPDATE kalitexnis SET onoma="%s", epitheto="%s", etos_gen=%s WHERE ar_taut="%s"' % tup)

    conn.commit()

    cur.close()
    conn.close()

    return '''Artist updated!'''

@route('/presentation_of_songs')
def show_pres_songs():
       return '''
<style type="text/css">
	p1 {
		padding-left: 35%;
	}
	p2 {
		padding-left: 8.2%;
	}
	p3 {
		padding-left: 5.2%;
	}
	p4 {
		padding-left: 10.2%;
	}
	p5 {
		padding-left: 3.2%;
	}
	p6 {
		padding-left: 2%;
	}
	p7 {
		padding-left: 0.35%;
	}
	p8 {
		padding-left: 3.6%;
	}

	h1 {
		font-size: 2em;
	}
</style>

<form accept-charset="UTF-8" method="post">
	<h1><p1><strong>&bull; Presentation Of Songs</strong></p1></h1>
	<hr>
	<p1><p6>Song Title<p5><input type="text" name="title"></p5></p6></p1><br>
	<p1><p6>Production Year<p7><input type="text" name="prodYear"></p7></p6></p1><br>
	<p1><p6>Company<p8><input type="text" name="company"></p8></p6></p1><br><br>
	<p1><p4><input type="submit" value="Submit"></p4></p1>
	<hr>
</form>
'''

@route('/presentation_of_songs', method='POST')
def pres_songs():
    conn=pymysql.connect(
        settings.mysql_host,
        settings.mysql_user,
        settings.mysql_passwd,
        settings.mysql_schema,
        charset='utf8')

    cur=conn.cursor()

    s1=' AND titlos="%s" '
    s2=' AND etos_par=%s '
    s3=' AND etaireia="%s" '
    
    a1=request.forms.get('title')
    a2=request.forms.get('prodYear')
    a3=request.forms.get('company')
    tup=(a1,a2,a3)

    if a1=='':
        s1='%s'
    if a2=='':
        s2='%s'
    if a3=='':
        s3='%s'
    stmt='SELECT titlos,etos_par,etaireia FROM cd_production RIGHT JOIN (SELECT * FROM tragoudi LEFT JOIN singer_prod ON title=titlos) AS A ON cd=code_cd WHERE 1=1'+s1+s2+s3
    cur.execute(stmt % tup)

    test_tuple=cur.fetchall()

    cur.close()
    conn.close()

    return template('trump.tpl',result = test_tuple)

@route('/insert_artists')
def show_ins_artist():
    return '''
<style type="text/css">
	p1 {
		padding-left: 35%;
	}
	p2 {
		padding-left: 8.2%;
	}
	p3 {
		padding-left: 5.2%;
	}
	p4 {
		padding-left: 0.75%;
	}
	p5 {
		padding-left: 3.2%;
	}
	p6 {
		padding-left: 1.4%;
	}
	p7 {
		padding-left: 0.3%;
	}
	p8 {
		padding-left: 2.9%;
	}

	h1 {
		font-size: 2em;
	}
</style>

<form accept-charset="UTF-8" method="post">
	<h1><p1><p3><strong>&bull; Insert Artists</strong></p3></p1></h1>
	<hr>
	<p1><p5>National Id<p7><input type="text" name="id" required></p7></p5></p1><br>
	<p1><p5>Name<p8><input type="text" name="name" required></p8></p5></p1><br>
	<p1><p5>Surname<p6><input type="text" name="surname" required></p6></p5></p1><br>
	<p1><p5>Birth Year<p4><input type="number" name="year" min="1900" max="2010" style="width: 173px" required></p4></p5></p1><br><br>
	<p1><p2><input type="submit" value="Update Information"></p2></p1>
	<hr>
</form>
'''

@route('/insert_artists', method='POST')
def ins_artist():
    conn=pymysql.connect(
        settings.mysql_host,
        settings.mysql_user,
        settings.mysql_passwd,
        settings.mysql_schema,
        charset='utf8')

    cur=conn.cursor()

    tup=(request.forms.get('id'),request.forms.get('name'),request.forms.get('surname'),request.forms.get('year'))
    
    cur.execute('INSERT INTO kalitexnis (ar_taut, onoma, epitheto, etos_gen) VALUES ("%s", "%s", "%s", %s)' % tup)

    conn.commit()

    cur.close()
    conn.close()

    return '''<!DOCTYPE html>
<html>
<head>
	<title>
		Thank you!
	</title>
</head>
<body>
<script type="text/javascript">
	alert("Thank you for updating our database!");
</script>
</body>
</html>Artist added to database!'''

@route('/insert_songs')
def show_ins_songs():
    return '''
<head>
<style type="text/css">
	p1 {
		padding-left: 35%;
	}
	p2 {
		padding-left: 6%;
	}
	p3 {
		padding-left: 5.2%;
	}
	p4 {
		padding-left: 0.75%;
	}
	p5 {
		padding-left: 6.6%;
	}
	p6 {
		padding-left: 1.4%;
	}
	p7 {
		padding-left: 0.3%;
	}
	p8 {
		padding-left: 2.9%;
	}

	h1 {
		font-size: 2em;
	}
</style>
<meta charset="utf-8"> 
</head>
<form action="/insert_songs", method="post">
	<h1><p1><p3><strong>&bull; Insert Song</strong></p3></p1></h1>
	<hr>
	<p1><p6>Title<p2><input type="text" name="title" required></p2></p6></p1><br>
	<p1><p6>Production Year<p7><input type="text" name="year" required></p7></p6></p1><br>
	<p1><p6>CD<p5><select name="cds">
		<option value="400400">CD1</option>
		<option value="400401">CD2</option>
		<option value="400412">CD3</option>
		<option value="400420">CD4</option>
		<option value="400657">CD5</option>
		<option value="410000">CD6</option>
		<option value="410001">CD7</option>
		<option value="410003">CD8</option>
		<option value="410005">CD9</option>
		<option value="420430">CD10</option>
		<option value="420440">CD11</option>
		<option value="420450">CD12</option>
		<option value="420460">CD13</option>
		<option value="420470">CD14</option>
		<option value="420480">CD15</option>
		<option value="420490">CD16</option>
		<option value="500500">CD17</option>
		<option value="500510">CD18</option>
		<option value="600601">CD19</option>
		<option value="600602">CD20</option>
		<option value="600603">CD21</option>
		<option value="670670">CD22</option>
		<option value="670680">CD23</option>
	</select></p5></p6></p1><br>

	<p1><p6>Singer<select name="singers">
		<option value="A300001">A 300001</option>
		<option value="D214215">D 214215</option>
		<option value="G210210">G 210210</option>
		<option value="G214214">G 214214</option>
		<option value="G214214">H 214214</option>
		<option value="J214214">J 214214</option>
		<option value="W100100">W 100100</option>
		<option value="W100101">W 100101</option>
		<option value="X101101">X 101101</option>
		<option value="X200203">X 200203</option>
		<option value="X500501">X 500501</option>
		<option value="X800002">X 800002</option>
		<option value="X800003">X 800003</option>
	</select></p6></p1><br>

	<p1><p6>Composer<select name = "composers">
		<option value = "A214214">A 214214</option>
		<option value = "E214214">E 214214</option>
		<option value = "I214214">I 214214</option>
		<option value = "N214214">N 214214</option>
		<option value = "P214214">P 214214</option>
		<option value = "S214214">S 214214</option>
		<option value = "X100100">X 100100</option>
		<option value = "X101101">X 101101</option>
		<option value = "X101104">X 101104</option>
		<option value = "X200204">X 200204</option>
		<option value = "X800000">X 800000</option>
	</select></p6></p1><br>

	<p1><p6>Song Writer <select name="writers">
		<option value = "A210210">A 210210</option>
		<option value = "A300000">A 300000</option>
		<option value = "D214214">D 214214</option>
		<option value = "I214214">I 214214</option>
		<option value = "J210210">J 210210</option>
		<option value = "K210210">K 210210</option>
		<option value = "P214214">P 214214</option>
		<option value = "W100110">W 100110</option>
		<option value = "X101101">X 101101</option>
		<option value = "X101102">X 101102</option>
		<option value = "X101104">X 101104</option>
		<option value = "X200205">X 200205</option>
		<option value = "X200215">X 200215</option>
		<option value = "X200220">X 200220</option>
		<option value = "X300300">X 300300</option>
		<option value = "X300301">X 300301</option>
		<option value = "X300302">X 300302</option>
		<option value = "X400300">X 400300</option>
	</select></p6></p1><br>
	<p1> <p2> <p8> <input type="submit" value="Submit" style="width: 100px"> </p8> </p2> </p1>
	<hr>
</form>
'''

@route('/insert_songs',method='POST')
def ins_songs():
    conn=pymysql.connect(
        settings.mysql_host,
        settings.mysql_user,
        settings.mysql_passwd,
        settings.mysql_schema,
        charset='utf8')

    cur=conn.cursor()

    tup=(request.forms.get('title'),request.forms.get('year'),request.forms.get('composers'),request.forms.get('writers'))

    cur.execute('INSERT INTO tragoudi (titlos, etos_par, sinthetis, stixourgos) VALUES ("%s", %s, "%s", "%s")' % tup)

    conn.commit()

    tup2=(request.forms.get('cds'),request.forms.get('title'),request.forms.get('singers'))
    
    cur.execute('INSERT INTO singer_prod (cd, title, tragoudistis) VALUES ("%s", "%s", "%s")' % tup2)

    conn.commit()

    cur.close()
    conn.close()

    return '''<!DOCTYPE html>
<html>
<head>
	<title>
		Thank you!
	</title>
</head>
<body>
<script type="text/javascript">
	alert("Thank you for updating our database!");
</script>
</body>
</html>Song added to database!'''

run(host='localhost',port=9090)
