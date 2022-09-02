



fun_factorial (){

        facto=1

        for i in $(seq 1 1 $1)
        do
                facto=$(($facto*i))
        done
        echo $facto




}
u=20
n=$(fun_factorial $u)
r=17
m=$(fun_factorial $r)

echo $((n/m))






