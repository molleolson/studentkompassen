/**
 * Created by Sofie on 2016-04-07.
 */

console.log("The detected language is: " + localStorage.getItem("language"));
makeTranslation(localStorage.getItem("language"));
$(document).ready(function() {
    function makeTranslation(language) {
        $('#middleboxJustnu').hide();
        if (localStorage.getItem("language") == null) {
            language = "english";
            console.log("no stored language")
        } else if (language == "other") {
            if (localStorage.getItem("language") == "swedish") {
                language = "english";
                console.log("Changed language to english")
            } else {
                language = "swedish";
                console.log("Changed language to Swedish")
            }
        }
        $.ajax({
            url: 'languages.xml',

            success: function (xml) {
                $(xml).find('translation').each(function () {
                    var id = $(this).attr('id');
                    var text = $(this).find(language).text();
                    $("." + id).html(text);
                });
                console.log("made a translation to: " + language + " :)");
                localStorage.setItem("language", language);
            }
        });
    }
});
