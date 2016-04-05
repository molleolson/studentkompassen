/**
 * Created by Sofie on 2016-04-05.
 */

$(document).ready(function(){
    $('#btnClick').on('click',function(){
        if($('#1').css('display')!='none'){
            $('#2').show();
            $('#1').hide();
        }else if($('#2').css('display')!='none'){
            $('#1').show();
            $('#2').hide();
        }
    });
});
$(document).ready(function(){
    $('#justnuklick').on('click',function(){
        if($('#middleboxJustnu').css('display')!='none'){

            $('#middleboxJustnu').hide();
        }else {
            $('#middleboxJustnu').show();

        }
    });
});