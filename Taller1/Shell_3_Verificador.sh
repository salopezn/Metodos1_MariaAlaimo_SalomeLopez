
pass=0
fail="Inente de nuevo con otro parametro"




fun_checkvalue (){

	if [[ 1 -eq "$1" ]] || [[ 0 -eq "$1" ]];then
		let "pass=1"
	else
		echo $fail

	fi

} 


while [ 0 -eq "$pass" ]

do
        read -p "Ingresar variable: " $1
        fun_checkvalue $1

done

