<!DOCTYPE html>
<html>

<head>
	<meta charset=utf-8/>
	<style type="text/css">
		p0 {
			padding-left: 40px;
		}
		p1 {
			padding-left: 60px;
		}
		h1 {
			font-size: 2em;
		}
	</style>
</head>

<body>
	<form>
		<h1><strong>View Artist Results</strong></h1><br>
		<hr>
		<b>Song Title<p0>Production Year</p0> <p0>Company</p0></b><br>
	
	</form>
	% for row in result:
   		{{row[0]}}, <p1>{{row[1]}},</p1> <p1>{{row[2]}}</p1>
   		<br>
	% end
	<hr>
</body>

</html>