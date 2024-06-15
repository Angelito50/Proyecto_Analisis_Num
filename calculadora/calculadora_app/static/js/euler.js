document.getElementById('continuarBtn').addEventListener('click', function(event) {
    event.preventDefault();
    const funcionF = document.getElementById('ecuacion').value;
    const pasoH = parseFloat(document.getElementById('h').value);
    const numPasos = parseInt(document.getElementById('numPasos').value);

    if (funcionF && !isNaN(xInicial) && !isNaN(yInicial) && !isNaN(pasoH) && !isNaN(numPasos)) {
        console.log("Función f(x, y):", funcionF);
        console.log("Tamaño del paso h:", pasoH);
        console.log("Número de pasos:", numPasos);
      
    } else {
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Por favor, llene todos los campos correctamente!'
        });
    }
});

document.addEventListener('DOMContentLoaded', function() {
    const continuarBtn = document.getElementById('continuarBtn');
    const spanRespuesta = document.getElementById('spanRespuesta');
    const resultadoFuncion = document.getElementById('resultadoFuncion');
    const textoEjemplo = document.getElementById('textoEjemplo');

    continuarBtn.addEventListener('click', function(event) {
        event.preventDefault(); // Evitar que el formulario se envíe por defecto

        // Obtener los valores de los input
        const funcionF = document.getElementById('ecuacion').value;
        const pasoH = document.getElementById('h').value;
        const numPasos = document.getElementById('numPasos').value;

        // Construir el texto para el span de respuesta
        const textoRespuesta = `Tu resultado de la ecuacion (${funcionF}), con número de pasos=${numPasos} y tamaño del paso h=${pasoH} es:`;

        // Actualizar el contenido del span y de los párrafos
        spanRespuesta.textContent = textoRespuesta;
        resultadoFuncion.textContent = funcionF;
        textoEjemplo.textContent = 'Texto de ejemplo';
    });
});
