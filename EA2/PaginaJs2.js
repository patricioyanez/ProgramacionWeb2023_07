function sumar()
{
    // value obtiene el valor actual del input
    let n1 = document.getElementById("numero1").value;
    let n2 = document.getElementById("numero2").value;
    if(n1 == "")
    {
        alert("Valor no especificado");
        return;
    }
    
    // parseInt => convierte un string en int
    let total = parseInt("0" + n1) + parseInt("0" + n2);
    alert("El resultado es: " + total);
}


// Ejercicios: Agregar botones y funciones para realizar:
// resta, multiplicación y división (evitar dividir por cero).
// y que no esten vacios

function restar()
{
    // value obtiene el valor actual del input
    let n1 = document.getElementById("numero1").value;
    let n2 = document.getElementById("numero2").value;
    // parseInt => convierte un string en int
    let total = parseInt(n1) - parseInt(n2);
    alert("El resultado es: " + total);
}
function multiplicar()
{
    // value obtiene el valor actual del input
    let n1 = document.getElementById("numero1").value;
    let n2 = document.getElementById("numero2").value;
    // parseInt => convierte un string en int
    let total = parseInt(n1) * parseInt(n2);
    alert("El resultado es: " + total);
}
function dividir()
{
    // value obtiene el valor actual del input
    let n1 = document.getElementById("numero1").value;
    let n2 = document.getElementById("numero2").value;
    // parseInt => convierte un string en int
    n1 = parseInt(n1);
    n2 = parseInt(n2);

    if(n2 == 0)
    {
        alert("No se puede dividir por cero.");
        return;
    }
    alert("El resultado es: " + n1/n2);
}
