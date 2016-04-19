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
    $('#datepicker').datepicker('setDate', eventDate);
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
    weekday[0] = "Sunday";
    weekday[1] = "Monday";
    weekday[2] = "Tuesday";
    weekday[3] = "Wednesday";
    weekday[4] = "Thursday";
    weekday[5] = "Friday";
    weekday[6] = "Saturday";

    var day = weekday[eventDate.getDay()];
    document.getElementById("getDay").innerHTML = day;

    var date = eventDate.getDate();
    document.getElementById("getDate").innerHTML = date;

    var monthList = new Array(12);

    monthList[0] = "January";
    monthList[1] = "February";
    monthList[2] = "Mars";
    monthList[3] = "April";
    monthList[4] = "May";
    monthList[5] = "June";
    monthList[6] = "July";
    monthList[7] = "August";
    monthList[8] = "September";
    monthList[9] = "October";
    monthList[10] = "November";
    monthList[11] = "December";

    var month = monthList[eventDate.getMonth()];
    document.getElementById("getMonth").innerHTML = month;
}

/**
 * Created by ebbaholmstrom on 16-04-18.
 */
$(function() {
    $( "#datepicker" ).datepicker({
        onSelect: function()
        {
            var date = $(this).datepicker('getDate');
            eventDate = date;
            writeDate();
        }
    });
});