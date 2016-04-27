/**
 * Created by facebook on 2016-04-25.
 */

  window.fbAsyncInit = function() {
    FB.init({
      appId      : '464984813707743',
      xfbml      : true,
      version    : 'v2.6'
    });
  };

  (function(d, s, id){
     var js, fjs = d.getElementsByTagName(s)[0];
     if (d.getElementById(id)) {return;}
     js = d.createElement(s); js.id = id;
          if(window.location.href.indexOf("/sv/") > -1) {
       var sprak = 'sv_SE';
    }
      else if(window.location.href.indexOf("/nb/") > -1) {
       var sprak = 'nb_NO';
    }
      else if(window.location.href.indexOf("/en/") > -1) {
       var sprak = 'en_US';
    }
      else{
         var sprak = 'sv_SE';
     } 
     js.src = "//connect.facebook.net/"+sprak+"/sdk.js";
     fjs.parentNode.insertBefore(js, fjs);
   }(document, 'script', 'facebook-jssdk'));


/* en_US för engelska */
/* sv_SE för svenska */
/* nb_NO för norska bokmål */
/* https://www.facebook.com/translations/FacebookLocales.xml - fullständig lista */