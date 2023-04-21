$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', {"hello" : "Salut"}, function (txt) {
    $('DIV#hello').append(txt.hello);
})