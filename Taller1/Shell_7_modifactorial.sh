fun_factorial (){
        facto=1
        for i in $(seq 1 1 $1)
        do
                facto=$(($facto*i))
        done
        echo $facto
}
read -p "Ingresar un valor: " x
for i in $(seq 1 1 $x)
do
	factor=$(fun_factorial $i)
	echo $factor
done
