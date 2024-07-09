$(document).ready(function() {
    $("#career-stats-table").show();
    $("#personal-info-table").hide();
    $("#awards-table").hide();
    $("#stat-graph").show();
    $("#progresion-graphs").hide();
    
    $("#toggle-stats").click(function() {
        $("#career-stats-table").show();
        $("#personal-info-table").hide();
        $("#awards-table").hide();
        $("#stat-graph").show();
        $("#progresion-graphs").hide();
    });
    $("#toggle-progression").click(function() {
        $("#career-stats-table").hide();
        $("#personal-info-table").hide();
        $("#awards-table").hide();
        $("#stat-graph").hide();
        $("#progresion-graphs").show();
    });
    $("#toggle-info").click(function() {
        $("#career-stats-table").hide();
        $("#personal-info-table").show();
        $("#awards-table").hide();
        $("#stat-graph").hide();
        $("#progresion-graphs").hide();
    });
    $("#toggle-awards").click(function() {
        $("#career-stats-table").hide();
        $("#personal-info-table").hide();
        $("#awards-table").show();
        $("#stat-graph").hide();
        $("#progresion-graphs").hide();
    });
});