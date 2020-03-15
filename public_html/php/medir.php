<?php
// Ejecuta como root, el script python encargado de controlar el sensor ultrasonido

echo exec('sudo python /var/www/html/cinematik_v1/python/calcular_datos.py');

//crear un archivo .py para cada operación así como la llamada ajax desde el html

// La salida la imprime con el echo

?>