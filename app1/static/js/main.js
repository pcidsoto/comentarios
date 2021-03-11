function mostrarErroresEdicion(errores) {
    $('#erroresEdicion').html("");
    let error = "";
    for (let item in errores.responseJSON.error) {
        error += '<div class = "alert alert-danger" <strong>' + errores.responseJSON.error[item] + '</strong></div>';
    }
    $('#erroresEdicion').append(error);
}

function cerrar_modal_edicion() {
    $('#edicion').modal('hide');
    setTimeout(function () {
        window.location.reload(1);
    }, 5000);
}

function editar() {
    var form = $('#form_edicion').serialize();
    //console.log("form: ", form);
    $.ajax({
        data: $('#form_edicion').serialize(),
        url: $('#form_edicion').attr('action'),
        type: $('#form_edicion').attr('method'),
        success: function (response) {
            notificacionSuccess2(response.mensaje);
            cerrar_modal_edicion();
        },
        error: function (error) {
            notificacionError(error.responseJSON.mensaje);
            mostrarErroresEdicion(error);

        }
    });
}

function notificacionError(mensaje) {
    Swal.fire({
        title: 'Error!',
        text: mensaje,
        icon: 'error'
    })
}

function notificacionSuccess(mensaje) {
    Swal.fire({
        title: 'Buen Trabajo!',
        text: mensaje,
        icon: 'success'
    })
}

//Recarga pagina al precionar ok
function notificacionSuccess2(mensaje) {
    Swal.fire({
        title: "Buen Trabajo!",
        text: mensaje,
        icon: "success"
    }).then(okay => {
        if (okay) {
            window.location.reload();
        }
    });
}