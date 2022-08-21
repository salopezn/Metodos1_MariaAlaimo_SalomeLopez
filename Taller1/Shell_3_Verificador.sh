
pass=0
fun_checkvalue (){

	if [[ 0 -eq "$1"]] || [[0 -eq "$1"]]

	then 
	     let pass=1
	else
	     echo "Intente denuevo con otro parametro"

	echo $pass
	fi
 } 

fun_checkvalue $1


