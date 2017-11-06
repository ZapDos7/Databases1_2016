<!DOCTYPE html>
<html>

<head>
	<meta charset=utf-8/>
	<style type="text/css">
		p0 {
			padding-left: 10px;
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
		<b>National ID <p0>Name</p0> <p0>Surname</p0> <p0>Birth Year</p0> <p0>Edit?		</p0></b><br>
	
	</form>
	% for row in result:
   		<form action="/presentation_of_artists/update">
   		{{row[0]}}, {{row[1]}}, {{row[2]}}, {{row[3]}} <input type="submit" value="Edit Me!">
   		</form>
	% end
</body>

</html>
