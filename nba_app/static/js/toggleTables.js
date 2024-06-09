$(document).ready(function() {
    $("#toggle-stats").click(function() {
        $("#personal-info-table").hide();
        $("#career-stats-table").show();
    });
    $("#toggle-info").click(function() {
        $("#career-stats-table").hide();
        $("#personal-info-table").show();
    });
});