from bottle import route, error, post, get, run, static_file, abort, redirect, response, request, template
import pymysql
import settings

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
        charset="utf8")

    cur=conn.cursor()

    #dict={ 'firstname' : request.forms.getunicode('firstname'), 'lastname' : request.forms.getunicode('lastname'), 'birthfrom' : request.forms.get('birthfrom'), 'birthto' : request.forms.get('birthto'), 'occupation' : request.forms.get('occupation')}

    
    
    select_stmt=('''SELECT * FROM kalitexnis WHERE onoma=%s AND epitheto=%s AND etos_gen>=%s AND etos_gen<=%s AND ar_taut IN (SELECT %s FROM singer_prod INNER JOIN (SELECT * from tragoudi)AS A ON title=titlos)''')
    tup=(request.forms.getunicode('firstname'),request.forms.getunicode('lastname'),request.forms.get('birthfrom'),request.forms.get('birthto'),request.forms.get('occupation'))
    cur.execute(select_stmt,tup)
# 
#
    test_tuple=cur.fetchall()

    cur.close()
    conn.close()

    return template('temp.tpl', result = test_tuple)
run(host='localhost',port=9090)
