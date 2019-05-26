function showalert(message, alerttype) {

    $('#alert_placeholder').append('<div id="alertdiv" class="alert ' + alerttype + '"><a class="close" data-dismiss="alert">×</a><span>' + message + '</span></div>')

    setTimeout(function () {


        $("#alertdiv").remove();

    }, 3000);
}


$(".delete").click(function () {
    var id = $(this).data("id"),
        page = $(this).data("page");
    $.ajax({
        url: '/teacher/delete',
        type: 'POST',
        data: {
            'id': id,
            'page': page,
            'csrfmiddlewaretoken': '{{ csrf_token }}',
            processData: false,
            contentType: false
        },

        success: function (json) {
            showalert('Учитель удалён', 'alert-success');
            document.getElementById(id).style.display = 'none';
            console.log('success');
        },

        error: function (xhr, errmsg, err) {
            console.log(xhr.status + ': ' + xhr.responseText);
        }
    });
});

function delete_complaint() {
    console.log('yayayayaya');
    var id = $(this).data("id"),
        page = $(this).data("page");
    $.ajax({
        url: '/complaint/delete',
        type: 'POST',
        data: {
            'id': id,
            'page': page,
            'csrfmiddlewaretoken': '{{ csrf_token }}',
            processData: false,
            contentType: false
        },

        success: function (json) {
            showalert('Жалоба удалёна', 'alert-success');
            document.getElementById(id).style.display = 'none';
            console.log('success');
        },

        error: function (xhr, errmsg, err) {
            console.log(xhr.status + ': ' + xhr.responseText);
        }
    });
};