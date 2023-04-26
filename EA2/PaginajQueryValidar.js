$(function()
{
    // codigo jQuery

    let numeros = '1234567890';
    let letras  = 'qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNMÁÉÍÓÚáéíóú';

    $('.txtRut').keypress(function(e)
    {
        let caracter = String.fromCharCode(e.which);
        if(numeros.indexOf(caracter) < 0)
            return false; // no dibuja el carecter de la tecla
    })
    $('.txtDv').keypress(function(e)
    {
        let caracter = String.fromCharCode(e.which);
        let patron = numeros + 'kK'
        if(patron.indexOf(caracter) < 0)
            return false; // no dibuja el carecter de la tecla
    })

    $('.btnLimpiar').click(function()
    {
        $('.txtRut, .txtDv, .txtNombre, .txtEmail').val('');
        $('.txtRut').focus();
    })
    $('.btnAceptar').click(function()
    {
        // validar campos vacios
        if(!$('.txtRut').val())
        {
            alert('Falta especificar el número de rut');
            $('.txtRut').focus();
        }
        else if(!$('.txtDv').val())
        {
            alert('Falta especificar el dv');
            $('.txtDv').focus();
        }
        else if(!$('.txtNombre').val())
        {
            alert('Falta especificar el nombre');
            $('.txtNombre').focus();
        }
        else if(!$('.txtEmail').val())
        {
            alert('Falta especificar el email');
            $('.txtEmail').focus();
        }
    })




});