
function_help() {
	echo "Debe incluir 3 parametros"
}

if ! [ $# -eq 3 ]; then
	function_help
	exit 1
else
	echo "Corriendo programa"

fi

