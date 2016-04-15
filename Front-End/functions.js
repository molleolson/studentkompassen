/**
 * Created by Sofie on 2016-04-05.
 */

$(document).ready(function(){
    $("#rnClick").click(function(){
        $("#rightNow").collapse('show');
        $("#breakfast,#lunch, #brunch,#fika,#pub, #club, #event, #ourEvent,#profile, #map, #getToKnowNations,#myEvents").collapse('hide');
        $("#rnL").attr('class','active');
        $("#bfL,#lunchL,#brunchL, #fikaL, #pubL,#clubL,#eventL,#ourEventL,#profileL,#getToKnowNationL,#myEventL").attr('class',null);

    });
    $("#bfClick").click(function(){
        $("#breakfast").collapse('show');
        $("#lunch, #brunch,#fika,#pub, #club, #event, #rightNow, #getToKnowNations,#myEvents").collapse('hide');
        $("#bfL").attr('class','active');
        $("#rnL,#lunchL,#brunchL, #fikaL, #pubL,#clubL,#eventL,#getToKnowNationL,#myEventL").attr('class',null);
    });
    $("#lunchClick").click(function(){
        $("#lunch").collapse('show');
        $("#breakfast, #brunch,#fika,#pub, #club, #event, #rightNow, #getToKnowNations,#myEvents").collapse('hide');
        $("#lunchL").attr('class','active');
        $("#bfL,#rnL,#brunchL, #fikaL, #pubL,#clubL,#eventL,#getToKnowNationL,#myEventL").attr('class',null);
    });
    $("#brunchClick").click(function(){
        $("#brunch").collapse('show');
        $("#breakfast,#lunch,#fika,#pub, #club, #event, #rightNow, #getToKnowNations,#myEvents").collapse('hide');
        $("#brunchL").attr('class','active');
        $("#bfL,#lunchL,#rnL, #fikaL, #pubL,#clubL,#eventL,#getToKnowNationL,#myEventL").attr('class',null);
    });
    $("#fikaClick").click(function(){
        $("#fika").collapse('show');
        $("#breakfast,#lunch, #brunch,#pub, #club, #event, #rightNow, #getToKnowNations,#myEvents").collapse('hide');
        $("#fikaL").attr('class','active');
        $("#bfL,#lunchL,#brunchL, #rnL, #pubL,#clubL,#eventL,#getToKnowNationL,#myEventL").attr('class',null);
    });
    $("#pubClick").click(function(){
        $("#pub").collapse('show');
        $("#breakfast,#lunch, #brunch,#fika,#club, #event, #rightNow, #getToKnowNations,#myEvents").collapse('hide');
        $("#pubL").attr('class','active');
        $("#bfL,#lunchL,#brunchL, #fikaL, #rnL,#clubL,#eventL,#getToKnowNationL,#myEventL").attr('class',null);
    });
    $("#clubClick").click(function(){
        $("#club").collapse('show');
        $("#breakfast,#lunch, #brunch,#fika,#pub, #event, #rightNow, #getToKnowNations,#myEvents").collapse('hide');
        $("#clubL").attr('class','active');
        $("#bfL,#lunchL,#brunchL, #fikaL, #pubL,#rnL,#eventL,#getToKnowNationL,#myEventL").attr('class',null);
    });
    $("#myEventsClick").click(function(){
        $("#myEvents").collapse('show');
        $("#breakfast,#lunch, #brunch,#fika,#pub, #event, #rightNow, #getToKnowNations").collapse('hide');
        $("#myEventL").attr('class','active');
        $("#bfL,#lunchL,#brunchL, #fikaL, #pubL,#rnL,#eventL,#getToKnowNationL,#clubL").attr('class',null);
    });
    $("#eventClick").click(function(){
        $("#event").collapse('show');
        $("#breakfast,#lunch, #brunch,#fika,#pub, #club, #rightNow, #ourEvent,#profile, #map, #getToKnowNations").collapse('hide');
        $("#eventL").attr('class','active');
        $("#bfL,#lunchL,#brunchL, #fikaL, #pubL,#clubL,#rnL,#ourEventL,#profileL,#getToKnowNationL").attr('class',null);
    });
    $("#knowClick").click(function(){
        $("#getToKnowNations").collapse('show');
        $("#breakfast,#lunch, #brunch,#fika,#pub, #club, #rightNow, #event,#myEvents").collapse('hide');
        $("#getToKnowNationL").attr('class','active');
        $("#bfL,#lunchL,#brunchL, #fikaL, #pubL,#clubL,#rnL,#ourEventL,#profileL,#eventL,#myEventL").attr('class',null);
    });

    $("#oeClick").click(function(){
        $("#ourEvent").collapse('show');
        $("#event, #rightNow,#profile,#map").collapse('hide');
        $("#ourEventL").attr('class','active');
        $("#eventL,#rnL,#profileL").attr('class',null);
    });

    $("#profileClick").click(function(){
        $("#profile,#map").collapse('show');
        $("#event, #rightNow,#ourEvent").collapse('hide');
        $("#profileL").attr('class','active');
        $("#eventL,#rnL,#ourEventL").attr('class',null);
    });
});
