#A.M. = 1115201400044, Ioanna Zapalidi, sdi1400044@di.uoa.gr

1. select etaireia, count(etaireia) as Synolo 
from cd_production 
group by etaireia
2. select titlos 
from tragoudi 
where sinthetis=stixourgos
3. select title 
from singer_prod 
group by title 
having count(title) > 1;
4. select ar_taut,onoma,epitheto, count(distinct cd) as Synolo
 from kalitexnis, singer_prod 
where kalitexnis.ar_taut = singer_prod.tragoudistis 
group by ar_taut;
5. select singer_prod.title
 from singer_prod, group_prod 
where singer_prod.title = group_prod.title;

6. select onoma, epitheto 
from 
(select onoma, epitheto, titlos 
from kalitexnis 
inner join tragoudi 
on kalitexnis.ar_taut = tragoudi.sinthetis 
) as ekto 
inner join singer_prod 
on ekto.titlos = singer_prod.title 
group by epitheto 
having count(distinct tragoudistis) = 1 
and epitheto not in  
(select epitheto 
from  
( 
select onoma, epitheto, titlos 
from kalitexnis 
inner join tragoudi 
on kalitexnis.ar_taut = tragoudi.sinthetis 
) as toidioekto 
inner join group_prod 
on toidioekto.titlos = group_prod.title 
)
7. select distinct title 
from group_prod 
where title not in 
(
select title 
from singer_prod
)

