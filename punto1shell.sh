read -p "Este programa calcula el factorial. Porfavor debe ingresar un numero: " x
fun_factorial (){
	facto=1
	for i in $(seq 1 1 $x)
	do
		facto=$(($facto*i))
	done 
	echo $facto

}

fun_factorial $x
