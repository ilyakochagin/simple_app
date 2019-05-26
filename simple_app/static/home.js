function showalert(message, alerttype) {
    $('#alert_placeholder').append('<div id="alertdiv" class="alert ' + alerttype + '"><a class="close" data-dismiss="alert">×</a><span>' + message + '</span></div>')

    setTimeout(function () {


        $("#alertdiv").remove();

    }, 3000);
}


$(".delete_teacher").click(function () {
    var id = $(this).data("id");
    console.log("iii", $(this).data(), id);
    $.ajax({
        url: '/teacher/delete',
        type: 'POST',
        data: {
            'id': id,
            'csrfmiddlewaretoken': '{{ csrf_token }}',
            processData: false,
            contentType: false
        },

        success: function (json) {
            showalert('Учитель удалён', 'alert-success');
            document.getElementById('teacher-row-'+id).style.display = 'none';
            console.log('success');
        },

        error: function (xhr, errmsg, err) {
            console.log(xhr.status + ': ' + xhr.responseText);
        }
    });
});

$(".delete_complaint").click(function () {
    console.log("sdfsdfsdf");
    var id = $(this).data("id");
    console.log("iii", $(this).data(), id);
    $.ajax({
        url: '/complaint/delete',
        type: 'POST',
        data: {
            'id': id,
            'csrfmiddlewaretoken': '{{ csrf_token }}',
            processData: false,
            contentType: false
        },

        success: function (json) {
            showalert('Жалоба удалёна', 'alert-success');
            document.getElementById('complaint-row-'+id).style.display = 'none';
            console.log('success');
        },

        error: function (xhr, errmsg, err) {
            console.log(xhr.status + ': ' + xhr.responseText);
        }
    });
});

$(".delete_review").click(function () {
    console.log("delete_review");
    var id = $(this).data("id");
    console.log("iii", $(this).data(), id);
    $.ajax({
        url: '/review/delete',
        type: 'POST',
        data: {
            'id': id,
            'csrfmiddlewaretoken': '{{ csrf_token }}',
            processData: false,
            contentType: false
        },

        success: function (json) {
            showalert('Отзыв удалён', 'alert-success');
            document.getElementById('review-row-'+id).style.display = 'none';
            console.log('success');
        },

        error: function (xhr, errmsg, err) {
            console.log(xhr.status + ': ' + xhr.responseText);
        }
    });
});