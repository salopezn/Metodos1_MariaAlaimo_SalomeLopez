
read -p "Ingresar el nombre del archivo de datos que quiere leer: " $nombredelarchivo


archivo="nombredelarchivo"
i=0
v=10
while read archivo;

do
	my_array=archivo
	echo $my_array[3]
	i=$((i+1))
done


