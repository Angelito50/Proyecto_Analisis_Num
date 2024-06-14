document.getElementById('cantidadPuntos').addEventListener('input', function(event) {
    let value = event.target.value;
    // Validamos que la entrada solo contenga dígitos y no esté vacía
    if (!/^\d*$/.test(value)) {
        Swal.fire({
            title: "<strong>Para escribir la cantidad de <u>Puntos (x , y)</u></strong>",
            icon: "info",
            html: `
              Escribe el numero dependiendo de la cantidad total de puntos que vayas a usar,
              ejemplo: <b>2</b>
            `,
            showCloseButton: true,
            focusConfirm: false,
            confirmButtonText: `
              <i class="fa fa-thumbs-up"></i> Entendido!
            `,
            confirmButtonAriaLabel: "Thumbs up, great!"
          });
        // Eliminamos cualquier carácter que no sea un dígito
        event.target.value = value.replace(/\D/g, '');
    }
});

document.getElementById('variablesXi').addEventListener('input', function(event) {
    let value = event.target.value;
    // Validamos que la entrada solo contenga dígitos y comas
    if (!/^[\d,]*$/.test(value)) {
        Swal.fire({
            title: "<strong>Solo puedes usar <u>Numeros y Comas</u></strong>",
            icon: "info",
            html: `
              Ejemplo: <b>1,2,3,4</b>,
              sin espacios.
            `,
            showCloseButton: true,
            focusConfirm: false,
            confirmButtonText: `
              <i class="fa fa-thumbs-up"></i> Entendido!
            `,
            confirmButtonAriaLabel: "Thumbs up, great!"
          });
        // Eliminamos cualquier carácter que no sea un dígito o coma
        event.target.value = value.replace(/[^,\d]/g, '');
    }
});

document.getElementById('variablesYi').addEventListener('input', function(event) {
    let value = event.target.value;
    // Validamos que la entrada solo contenga dígitos y comas
    if (!/^[\d,]*$/.test(value)) {
        Swal.fire({
            title: "<strong>Solo puedes usar <u>Numeros y Comas</u></strong>",
            icon: "info",
            html: `
              Ejemplo: <b>1,2,3,4</b>,
              sin espacios.
            `,
            showCloseButton: true,
            focusConfirm: false,
            confirmButtonText: `
              <i class="fa fa-thumbs-up"></i> Entendido!
            `,
            confirmButtonAriaLabel: "Thumbs up, great!"
          });
        // Eliminamos cualquier carácter que no sea un dígito o coma
        event.target.value = value.replace(/[^,\d]/g, '');
    }
});



document.getElementById('continuarBtn').addEventListener('click', function() {
    let cantidadPuntos = document.getElementById('cantidadPuntos').value.trim();
    let variablesXi = document.getElementById('variablesXi').value.trim();
    let variablesYi = document.getElementById('variablesYi').value.trim();
    
    // Validamos que los inputs no estén vacíos
    if (cantidadPuntos === '') {
        Swal.fire("'Por favor, ingrese la cantidad de puntos.");
        return; // Detenemos la ejecución del código
    }

    if (variablesXi === '') {
        Swal.fire("'Por favor, ingrese las variables Xi.");
        return; // Detenemos la ejecución del código
    }

    if (variablesYi === '') {
        Swal.fire("'Por favor, ingrese las variables Yi.");
        return; // Detenemos la ejecución del código
    }

    Swal.fire({
        position: "top-center",
        icon: "success",
        title: "Tu ejercicio esta siendo procesado con exito",
        showConfirmButton: false,
        timer: 1500
    });
});


document.addEventListener('DOMContentLoaded', () => {
  const continuarBtn = document.getElementById('continuarBtn');
  const spanRespuesta = document.getElementById('spanRespuesta');

  continuarBtn.addEventListener('click', (event) => {
      event.preventDefault(); // Evitar que el formulario se envíe

      // Obtener los valores de los inputs
      const cantidadPuntos = document.getElementById('cantidadPuntos').value;
      const variablesXi = document.getElementById('variablesXi').value;
      const variablesYi = document.getElementById('variablesYi').value;

      // Validar los inputs
      if (!cantidadPuntos || !variablesXi || !variablesYi) {
          Swal.fire({
              icon: 'error',
              title: 'Oops...',
              text: 'Por favor, llene todos los campos correctamente!'
          });
          return;
      }

      // Actualizar el contenido del span
      spanRespuesta.innerText = `La respuesta a tu ejercicio con el método de diferencias divididas con ${cantidadPuntos} puntos y los valores Xi: ${variablesXi} y Yi: ${variablesYi}`;
  });
});
