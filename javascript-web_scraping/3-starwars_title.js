#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';

request(url + process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const js = JSON.parse(body);
    console.log(js.title);
  } else {
    console.log(`Erro code: ${response.statusCode}`);
  }
});
