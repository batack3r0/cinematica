//Movimiento Rectilíneo Uniformemente Acelerado

$(document).ready(function () {
    $("#btnMedir").click(medir);
    $("#btnGraficar").click(graficar);
});

function medir() {
    $.ajax({
        url: "/php/medir.php",
        type: "POST"
    }).done(function (data) {
        var medir_data = " ";
        $.each(data.matches, function (key, value) {
            medir_data += "<tr>";
            medir_data += "<td>" + value.score.winner + "</td>";
            medir_data += "</tr>";
            $('#medir_tabla').append(medir_data);
        });
        console.log(data);
    });
}

function graficar() {
    $.ajax({
        url: "/php/graficar.php",
        type: "POST"
    }).done(function (data) {
        var graficar_data = " ";
        $.each(data.competitions, function (key, value) {
            graficar_data += "<tr>";
            graficar_data += "<td>" + value.name + "</td>";
            graficar_data += "</tr>";
            $('#graficar_tabla').append(graficar_data);
        });
        //console.log(data);
    });
}