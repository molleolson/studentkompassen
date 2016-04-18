/**
 * Created by ebbaholmstrom on 16-04-15.
 */
var eventDate = new Date();

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

function writeDate() {

    var weekday = new Array(7);
    weekday[0] = "Sunday";
    weekday[1] = "Monday";
    weekday[2] = "Tuesday";
    weekday[3] = "Wednesday";
    weekday[4] = "Thursday";
    weekday[5] = "Friday";
    weekday[6] = "Saturday";

    var n = weekday[eventDate.getDay()];
    document.getElementById("getDay").innerHTML = n;

    var q = eventDate.getDate();
    document.getElementById("getDate").innerHTML = q;

    var month = new Array(12);

    month[0] = "January";
    month[1] = "February";
    month[2] = "Mars";
    month[3] = "April";
    month[4] = "May";
    month[5] = "June";
    month[6] = "July";
    month[7] = "August";
    month[8] = "September";
    month[9] = "October";
    month[10] = "November";
    month[11] = "December";

    var b = month[eventDate.getMonth()];
    document.getElementById("getMonth").innerHTML = b;
}