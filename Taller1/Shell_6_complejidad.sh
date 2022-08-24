#número de operaciones que necesitas para llegar a la solución.
#entonces para el factorial de n(=20) la complejidad computacional seria 19
#para el factorial de n-r(17) la complejidad seria 16
#la complejidad total del algorito deberia ser 35

fun_complejos (){
	num=0

        for i in $(seq 1 1 $1)
        do
       		let "num=i-1"
        done

	echo $num




}

fun_complejos 37

