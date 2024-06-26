$(document).ready(function() {
    $("#career-stats-table").show();
    $("#personal-info-table").hide();
    $("#awards-table").hide();
    $("#graphs").hide();
    
    $("#toggle-stats").click(function() {
        $("#personal-info-table").hide();
        $("#career-stats-table").show();
        $("#awards-table").hide();
        $("#graphs").hide();
    });
    $("#toggle-graphs").click(function() {
        $("#personal-info-table").hide();
        $("#career-stats-table").hide();
        $("#awards-table").hide();
        $("#graphs").show();
    });
    $("#toggle-info").click(function() {
        $("#career-stats-table").hide();
        $("#personal-info-table").show();
        $("#awards-table").hide();
        $("#graphs").hide();
    });
    $("#toggle-awards").click(function() {
        $("#career-stats-table").hide();
        $("#personal-info-table").hide();
        $("#awards-table").show();
        $("#graphs").hide();
    });
});