function getKey() {
  var key = new Array();
  key['g'] = 'google',
  key['a'] = 'aur',
  key['w'] = 'wiki',

  isNetscape=(document.layers);
  eventChooser = (isNetscape) ? keyStroke.which : event.keyCode;
  which = String.fromCharCode(eventChooser).toLowerCase();

  for(var i in key) {
    if (which == i) {
      console.log(document.getElementById("search-text").focused);
      if(!document.getElementById("search-text").focused) {
        document.getElementById(key[i]).checked = true;
      }
    }
  }
}

window.onload = function() {
  var search_field = document.getElementById("search-text");

  search_field.focused = true;
  
  search_field.hasFocus = function() {
    return this.focused;
  }

  search_field.onfocus = function() {
    this.focused = true;
  }

  search_field.onblur = function() {
    this.focused = false;
  }

  document.getElementById('search-text').focus();
  document.getElementById('google').checked = true;

  document.onkeypress = getKey;
}

