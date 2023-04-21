$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', {"name" : ""}, function (txt) {
    $('DIV#character').append(txt.name);
})