$.getJSON("https://swapi-api.hbtn.io/api/films/?format=json", function(data) {
  const titles = data.results.map(function(mov) {
    return mov.title;
  });
  let $list = $('#list_movies');
  $.each(titles, function(i, movie_title) {
    $("<li>").text(movie_title).appendTo($list);
  });
});
