$(function () {

  /* Functions */

    // USING AJAX TO UPDATE DATABASE THROUGH REST API
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

    var loadForm = function () {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-person").modal("show");
            },
            success: function (data) {
                $("#modal-person .modal-content").html(data.html_form);
            }
        });
    };


    var saveForm = function () {
        /*var $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');*/
        var form = $(this);
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            beforeSend: function (xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
                },
            statusCode: {
                200: function () {
                    $.get("/updated_list/", function (data) {
                        $("#people-table").html(data.html_people_list);
                    });
                    $("#modal-person").modal("hide");
                },
                201: function () {
                    $.get("/updated_list/", function (data) {
                        $("#people-table").html(data.html_people_list);
                    });
                    $("#modal-person").modal("hide");
                },
                204: function () {
                    $.get("/updated_list/", function (data) {
                        $("#people-table").html(data.html_people_list);
                    });
                    $("#modal-person").modal("hide");  // <-- Close the modal
                },
            },
            error: function (xhr, statusText, err) {
                alert("Error:" + xhr.status);
            },
        });
        return false;
    };


    // Create person
    $(".js-person-create").click(loadForm);
    $("#modal-person").on("submit", ".js-person-create-form", saveForm);

    // Update person
    $("#people-table").on("click", ".js-update-person", loadForm);
    $("#modal-person").on("submit", ".js-person-update-form", saveForm);

    // Delete book
    $("#people-table").on("click", ".js-delete-person", loadForm);
    $("#modal-person").on("submit", ".js-person-delete-form", saveForm);

});
