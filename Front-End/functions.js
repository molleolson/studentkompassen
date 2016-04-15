/**
 * Created by Sofie on 2016-04-05.
 */

$(document).ready(function(){
    $("#rnClick").click(function(){
        $("#rightNow").collapse('show');
        $("#breakfast,#lunch, #brunch,#fika,#pub, #club, #event").collapse('hide');
        $("#rnL").attr('class','active');
        $("#bfL,#lunchL,#brunchL, #fikaL, #pubL,#clubL,#eventL").attr('class',null);

    });
    $("#bfClick").click(function(){
        $("#breakfast").collapse('show');
        $("#lunch, #brunch,#fika,#pub, #club, #event, #rightNow").collapse('hide');
        $("#bfL").attr('class','active');
        $("#rnL,#lunchL,#brunchL, #fikaL, #pubL,#clubL,#eventL").attr('class',null);
    });
    $("#lunchClick").click(function(){
        $("#lunch").collapse('show');
        $("#breakfast, #brunch,#fika,#pub, #club, #event, #rightNow").collapse('hide');
        $("#lunchL").attr('class','active');
        $("#bfL,#rnL,#brunchL, #fikaL, #pubL,#clubL,#eventL").attr('class',null);
    });
    $("#brunchClick").click(function(){
        $("#brunch").collapse('show');
        $("#breakfast,#lunch,#fika,#pub, #club, #event, #rightNow").collapse('hide');
        $("#brunchL").attr('class','active');
        $("#bfL,#lunchL,#rnL, #fikaL, #pubL,#clubL,#eventL").attr('class',null);
    });
    $("#fikaClick").click(function(){
        $("#fika").collapse('show');
        $("#breakfast,#lunch, #brunch,#pub, #club, #event, #rightNow").collapse('hide');
        $("#fikaL").attr('class','active');
        $("#bfL,#lunchL,#brunchL, #rnL, #pubL,#clubL,#eventL").attr('class',null);
    });
    $("#pubClick").click(function(){
        $("#pub").collapse('show');
        $("#breakfast,#lunch, #brunch,#fika,#club, #event, #rightNow").collapse('hide');
        $("#pubL").attr('class','active');
        $("#bfL,#lunchL,#brunchL, #fikaL, #rnL,#clubL,#eventL").attr('class',null);
    });
    $("#clubClick").click(function(){
        $("#club").collapse('show');
        $("#breakfast,#lunch, #brunch,#fika,#pub, #event, #rightNow").collapse('hide');
        $("#clubL").attr('class','active');
        $("#bfL,#lunchL,#brunchL, #fikaL, #pubL,#rnL,#eventL").attr('class',null);
    });
    $("#eventClick").click(function(){
        $("#event").collapse('show');
        $("#breakfast,#lunch, #brunch,#fika,#pub, #club, #rightNow").collapse('hide');
        $("#eventL").attr('class','active');
        $("#bfL,#lunchL,#brunchL, #fikaL, #pubL,#clubL,#rnL").attr('class',null);
    });

});
