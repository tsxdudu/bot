const { Client } = require('whatsapp-web.js');

const client = new Client();

client.on('qr', (qr) => {
  // Generate and scan this code with your phone
  console.log('QR RECEIVED', qr);
});

client.on('ready', () => {
  console.log('Client is ready!');

  // Send a message
  client.sendMessage('RECIPIENT_NUMBER', 'Hello, World!');
});

client.initialize();