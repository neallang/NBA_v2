$(document).ready(function() {
    $("#career-stats-table").show();
    $("#personal-info-table").hide();
    $("#awards-table").hide();
    
    $("#toggle-stats").click(function() {
        $("#personal-info-table").hide();
        $("#career-stats-table").show();
        $("#awards-table").hide();
    });
    $("#toggle-info").click(function() {
        $("#career-stats-table").hide();
        $("#personal-info-table").show();
        $("#awards-table").hide();
    });
    $("#toggle-awards").click(function() {
        $("#career-stats-table").hide();
        $("#personal-info-table").hide();
        $("#awards-table").show();

    });
});