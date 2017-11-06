# -*- coding : iso-8859-15 -*-
from bottle import route, error, post, get, run, static_file, abort, redirect, response, request, template
import pymysql
import settings

alpha_key=str()

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
	<p1><p2><p6><input type="radio" name="occupation" value="tragoudistis" checked="yes">Singer<br></p6></p2></p1>
	<p1>Type<p2><input type="radio" name="occupation" value="stixourgos">Song Writer<br></p2></p1>
	<p1><p2><p6><input type="radio" name="occupation" value="sinthetis">Composer</p6></p2></p1><br>
	<p0><p7><input type="submit" value="Submit"></p7></p0>
	<hr>
</form>
'''

@route('/presentation_of_artists', method='POST')
def bla():
    conn=pymysql.connect(
        settings.mysql_host,
        settings.mysql_user,
        settings.mysql_passwd,
        settings.mysql_schema,
        charset='utf8')

    cur=conn.cursor()

    tup=(request.forms.get('firstname'), request.forms.get('lastname') ,request.forms.get('birthfrom'),request.forms.get('birthto'),request.forms.get('occupation'))

    cur.execute("SELECT * FROM kalitexnis WHERE onoma='%s' AND epitheto='%s' AND etos_gen>=%s AND etos_gen<=%s AND ar_taut IN (SELECT %s FROM singer_prod INNER JOIN (SELECT * from tragoudi)AS A ON title=titlos)" % tup)
    test_tuple=cur.fetchall()

    global alpha_key
    for row in test_tuple:
        alpha_key=row[0]
        print alpha_key
    
    cur.close()
    conn.close()

    return template('temp.tpl', result = test_tuple)

@route('/')
def bloo():
    return '''
<hr>
<form align="center" action="/presentation_of_artists">
	<input type="submit" value="Update & Search Artists" style="width: 200px">
	<br>
</form>
<form align="center" action="presentation_of_songs.html">
	<input type="submit" value="Search Songs" style="width: 200px">
	<br>
</form>
<form align="center" action="insert_artists.html">
	<input type="submit" value="Insert Artists" style="width: 200px">
	<br>
</form>
<form align="center" action="insert_songs.html">
	<input type="submit" value="Insert Song" style="width: 200px">
</form>
<hr>
'''

@route('/presentation_of_artists/update')
def blo():
    global alpha_key
    print alpha_key
    return '''

'''

#@

run(host='localhost',port=9090)
