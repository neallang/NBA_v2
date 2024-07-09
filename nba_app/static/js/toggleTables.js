$(document).ready(function() {
    $("#career-stats-table").show();
    $("#personal-info-table").hide();
    $("#awards-table").hide();
    $("#stat-graph").show();
    
    $("#toggle-stats").click(function() {
        $("#career-stats-table").show();
        $("#personal-info-table").hide();
        $("#awards-table").hide();
        $("#stat-graph").show();
    });
    $("#toggle-progression").click(function() {
        $("#career-stats-table").hide();
        $("#personal-info-table").hide();
        $("#awards-table").hide();
        $("#stat-graph").hide();
    });
    $("#toggle-info").click(function() {
        $("#career-stats-table").hide();
        $("#personal-info-table").show();
        $("#awards-table").hide();
        $("#stat-graph").hide();
    });
    $("#toggle-awards").click(function() {
        $("#career-stats-table").hide();
        $("#personal-info-table").hide();
        $("#awards-table").show();
        $("#stat-graph").hide();
    });
});