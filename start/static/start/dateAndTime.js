/**
 * Created by ebbaholmstrom on 16-04-15.
 */
var eventDate = new Date();

/* START TEXT KOPPLAD TILL KALENDER */
$ (function() {
    writeDate();
    $(".glyphicon-chevron-right").click(function() {switchDate(1)});
    $(".glyphicon-chevron-left").click(function() {switchDate(-1)});

})

function switchDate(day){
    eventDate.setDate(eventDate.getDate() + day);
    writeDate();
    switchDateCalender(eventDate);
    /*$('#datepicker').datepicker('setDate', eventDate);*/
}

 
/* SLUT TEXT KOPPLAD TILL KALENDER */


/* START KALENDER KOPPLAD TILL TEXTEN */
/*
$("#dt").datepicker({
    onSelect: function(dateText, inst) {
        var date = $(this).val();
        var time = $('#time').val();
        alert('on select triggered');
        $("#start").val(date + time.toString(' HH:mm').toString());

    }
});
*/
/* SLUT KALENDER KOPPLAD TILL TEXTEN */

function writeDate() {

    var weekday = new Array(7);
    weekday[0] = gettext('Sunday');
    weekday[1] = gettext('Monday');
    weekday[2] = gettext('Tuesday');
    weekday[3] = gettext('Wednesday');
    weekday[4] = gettext('Thursday');
    weekday[5] = gettext('Friday');
    weekday[6] = gettext('Saturday');

    var day = weekday[eventDate.getDay()];
    document.getElementById("getDay").innerHTML = day;

    var date = eventDate.getDate();
    document.getElementById("getDate").innerHTML = date;

    var monthList = new Array(12);

    monthList[0] = gettext('January');
    monthList[1] = gettext('February');
    monthList[2] = gettext('March');
    monthList[3] = gettext('April');
    monthList[4] = gettext('May');
    monthList[5] = gettext('June');
    monthList[6] = gettext('July');
    monthList[7] = gettext('August');
    monthList[8] = gettext('September');
    monthList[9] = gettext('October');
    monthList[10] = gettext('November');
    monthList[11] = gettext('December');

    var month = monthList[eventDate.getMonth()];

    document.getElementById("getMonth").innerHTML = month;
}
