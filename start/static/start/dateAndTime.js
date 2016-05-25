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
    /*
    var weekdaysv = new Array(7);
    weekday[0] = "Söndag";
    weekday[1] = "Måndag";
    weekday[2] = "Tisdag";
    weekday[3] = "Onsdag";
    weekday[4] = "Torsdag";
    weekday[5] = "Fredag";
    weekday[6] = "Lördag";

    var daysv = weekdaysv[eventDate.getDay()];
    document.getElementById("getDaysv").innerHTML = daysv;

    var datesv = eventDate.getDate();
    document.getElementById("getDatesv").innerHTML = datesv;

    var monthListsv = new Array(12);

    monthList[0] = "Januari";
    monthList[1] = "Februari";
    monthList[2] = "Mars";
    monthList[3] = "April";
    monthList[4] = "Maj";
    monthList[5] = "Juni";
    monthList[6] = "Juli";
    monthList[7] = "Augusti";
    monthList[8] = "September";
    monthList[9] = "Oktober";
    monthList[10] = "November";
    monthList[11] = "December";

    var monthsv = monthListsv[eventDate.getMonth()];
    document.getElementById("getMonthsv").innerHTML = monthsv; */
}
