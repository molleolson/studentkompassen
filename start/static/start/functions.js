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
        $("#rightNow").collapse('hide');
        $("#lunch").collapse('hide');
        $("#brunch").collapse('hide');
        $("#fika").collapse('hide');
        $("#pub").collapse('hide');
        $("#club").collapse('hide');
        $("#event").collapse('hide');
        $("#bfL").attr('class','active');
        $("#rnL,#lunchL,#brunchL, #fikaL, #pubL,#clubL,#eventL").attr('class',null);
    });
    $("#lunchClick").click(function(){
        $("#lunch").collapse('show');
        $("#breakfast").collapse('hide');
        $("#rightNow").collapse('hide');
        $("#brunch").collapse('hide');
        $("#fika").collapse('hide');
        $("#pub").collapse('hide');
        $("#club").collapse('hide');
        $("#event").collapse('hide');
        $("#lunchL").attr('class','active');
        $("#bfL,#rnL,#brunchL, #fikaL, #pubL,#clubL,#eventL").attr('class',null);
    });
    $("#brunchClick").click(function(){
        $("#brunch").collapse('show');
        $("#rightNow").collapse('hide');
        $("#lunch").collapse('hide');
        $("#breakfast").collapse('hide');
        $("#fika").collapse('hide');
        $("#pub").collapse('hide');
        $("#club").collapse('hide');
        $("#event").collapse('hide');
        $("#brunchL").attr('class','active');
        $("#bfL,#lunchL,#rnL, #fikaL, #pubL,#clubL,#eventL").attr('class',null);
    });
    $("#fikaClick").click(function(){
        $("#fika").collapse('show');
        $("#breakfast").collapse('hide');
        $("#lunch").collapse('hide');
        $("#brunch").collapse('hide');
        $("#rightNow").collapse('hide');
        $("#pub").collapse('hide');
        $("#club").collapse('hide');
        $("#event").collapse('hide');
        $("#fikaL").attr('class','active');
        $("#bfL,#lunchL,#brunchL, #rnL, #pubL,#clubL,#eventL").attr('class',null);
    });
    $("#pubClick").click(function(){
        $("#pub").collapse('show');
        $("#rightNow").collapse('hide');
        $("#lunch").collapse('hide');
        $("#brunch").collapse('hide');
        $("#fika").collapse('hide');
        $("#breakfast").collapse('hide');
        $("#club").collapse('hide');
        $("#event").collapse('hide');
        $("#pubL").attr('class','active');
        $("#bfL,#lunchL,#brunchL, #fikaL, #rnL,#clubL,#eventL").attr('class',null);
    });
    $("#clubClick").click(function(){
        $("#club").collapse('show');
        $("#breakfast").collapse('hide');
        $("#lunch").collapse('hide');
        $("#brunch").collapse('hide');
        $("#rightNow").collapse('hide');
        $("#pub").collapse('hide');
        $("#fika").collapse('hide');
        $("#event").collapse('hide');
        $("#clubL").attr('class','active');
        $("#bfL,#lunchL,#brunchL, #fikaL, #pubL,#rnL,#eventL").attr('class',null);
    });
    $("#eventClick").click(function(){
        $("#event").collapse('show');
        $("#rightNow").collapse('hide');
        $("#lunch").collapse('hide');
        $("#brunch").collapse('hide');
        $("#fika").collapse('hide');
        $("#breakfast").collapse('hide');
        $("#club").collapse('hide');
        $("#pub").collapse('hide');
        $("#eventL").attr('class','active');
        $("#bfL,#lunchL,#brunchL, #fikaL, #pubL,#clubL,#rnL").attr('class',null);
    });
/* bytaspråk knappen*/
    $(".block").click(function(){
        $(".language-link .hidden").removeClass(".hidden")
        $(this).addClass("hidden")
        alert("Put a message here.")    })
});

