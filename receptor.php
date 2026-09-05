<?php
    require_once('./config/conexion.php');
    //isset() revisa si algo existe
    if(isset($_POST['Enviar'])){
        //crear una variable para guardar y transformar el dato
        $dolar = $_POST['dolares'];
        $euro = $dolar * 0.92;

        $sql = "INSERT INTO conversiones (dolares, euros) VALUES (?,?)";
        $stmt = $pdo -> prepare($sql);
        $stmt -> execute([$dolar, $euro]);
        echo("Conversión guardada: " . $euro);

    }