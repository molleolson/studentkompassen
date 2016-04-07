/**
 * Created by Sofie on 2016-04-05.
 */


$(document).ready(function(){
    $('#justnuklick').on('click',function(){
        if($('#middleboxJustnu').css('display')!='none'){

            /*$('#middleboxJustnu').hide();*/
        }else {
            $('#middleboxJustnu').show();
            $('#middleboxFrukost').hide();
            $('#middleboxLunch').hide();
            $('#middleboxFika').hide();
            $('#middleboxElse').hide();
            $('#middleboxKlubb').hide();
            $('#middleboxPub').hide();

        }
    });
});
$(document).ready(function(){
    $('#frukostklick').on('click',function(){
        if($('#middleboxFrukost').css('display')=='none')
            $('#middleboxJustnu').hide();
            $('#middleboxFrukost').show();
            $('#middleboxLunch').hide();
            $('#middleboxFika').hide();
            $('#middleboxElse').hide();
            $('#middleboxKlubb').hide();
            $('#middleboxPub').hide();


    });
});
$(document).ready(function(){
    $('#lunchklick').on('click',function(){
        if($('#middleboxLunch').css('display')=='none'){

            $('#middleboxJustnu').hide();
            $('#middleboxFrukost').hide();
            $('#middleboxPub').hide();
            $('#middleboxFika').hide();
            $('#middleboxElse').hide();
            $('#middleboxKlubb').hide();

            $('#middleboxLunch').show();

        }
    });
});
$(document).ready(function(){
    $('#fikaklick').on('click',function(){
        if($('#middleboxFika').css('display')=='none'){

            $('#middleboxJustnu').hide();
            $('#middleboxFrukost').hide();
            $('#middleboxLunch').hide();
            $('#middleboxPub').hide();
            $('#middleboxElse').hide();
            $('#middleboxKlubb').hide();

            $('#middleboxFika').show();

        }
    });
});
$(document).ready(function(){
    $('#pubklick').on('click',function(){
        if($('#middleboxPub').css('display')=='none'){

            $('#middleboxJustnu').hide();
            $('#middleboxFrukost').hide();
            $('#middleboxLunch').hide();
            $('#middleboxFika').hide();
            $('#middleboxElse').hide();
            $('#middleboxKlubb').hide();
            $('#middleboxPub').show();

        }
    });
});
$(document).ready(function(){
    $('#klubbklick').on('click',function(){
        if($('#middleboxKlubb').css('display')=='none'){

            $('#middleboxJustnu').hide();
            $('#middleboxFrukost').hide();
            $('#middleboxLunch').hide();
            $('#middleboxFika').hide();
            $('#middleboxPub').hide();
            $('#middleboxElse').hide();
            $('#middleboxKlubb').show();

        }
    });
});
$(document).ready(function(){
    $('#elseklick').on('click',function(){
        if($('#middleboxElse').css('display')=='none'){

            $('#middleboxJustnu').hide();
            $('#middleboxFrukost').hide();
            $('#middleboxLunch').hide();
            $('#middleboxFika').hide();
            $('#middleboxPub').hide();
            $('#middleboxKlubb').hide();
            $('#middleboxElse').show();

        }
    });
});