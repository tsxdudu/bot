const request = require('request');

const options = {
  method: 'POST',
  url: 'https://gate.whapi.cloud/messages/text?token=YOUR_API_TOKEN',
  headers: {accept: 'application/json', 'content-type': 'application/json'},
  body: {
    to: 'RECIPIENT_NUMBER',
    body: 'Hello, World!'
  },
  json: true
};

request(options, function (error, response, body) {
  if (error) throw new Error(error);

  console.log(body);
});