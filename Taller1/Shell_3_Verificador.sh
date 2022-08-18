
pass=0
fun_checkvalue (){
	$1


	if [[ $1=="0" || $1=="1"]]; then 
		pass=1
	else
		echo "Intente  denuevo con otro parametro"

fi




}

while read pass
do 


