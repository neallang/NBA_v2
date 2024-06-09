$(document).ready(function() {
    function setupAutocomplete(inputId) {
        $(inputId).autocomplete({
            source: function(request, response) {
                $.ajax({
                    url: "/",
                    dataType: "json",
                    data: {
                        q: request.term
                    },
                    success: function(data) {
                        response(data.map(player => player.full_name));
                    }
                });
            },
            minLength: 2,
            select: function(event, ui) {
                $(inputId).val(ui.item.value);
            }
        });
    }

    setupAutocomplete("#player1");
    setupAutocomplete("#player2");
});
