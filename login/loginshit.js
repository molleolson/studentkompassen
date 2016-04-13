/**
 * Created by ebbaholmstrom on 16-04-07.
 */
$('.message a').click(function(){
    $('form').animate({height: "toggle", opacity: "toggle"}, "slow");
});