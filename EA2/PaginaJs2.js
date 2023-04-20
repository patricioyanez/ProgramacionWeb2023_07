function sumar()
{
    // value obtiene el valor actual del input
    let n1 = document.getElementById("numero1").value;
    let n2 = document.getElementById("numero2").value;
    // parseInt => convierte un string en int
    let total = parseInt(n1) + parseInt(n2);
    alert("El resultado es: " + total);
}


// Ejercicios: Agregar botones y funciones para realizar:
// resta, multiplicación y división (evitar dividir por cero).
// y que no esten vacios