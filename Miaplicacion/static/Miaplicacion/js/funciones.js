document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("formulario").addEventListener('submit', validarFormulario); 
  });

  function validarFormulario(evento) {
    evento.preventDefault();
    var nombre = document.getElementById('nombre_contacto').value;
    if(nombre.length == 0) {
      alert('No has escrito nada en el nombre');
      return;
    }
    var email= document.getElementById('correo_contacto').value;
    if (email.length ==0) {
      alert('el correo no se ha ingresado');
      return;
    }
    var areatext= document.getElementById('mensaje_contacto').value;
    if (areatext.length < 18) {
      alert('Por favor escribe un mensaje');
      return;
    }
    this.submit();
  }

  //Para poder llamar el datatable
//npm install datatables.net    # Core library
//npm install datatables.net-dt # Styling
//var $  = require( 'jquery' );
//var dt = require( 'datatables.net' )();//