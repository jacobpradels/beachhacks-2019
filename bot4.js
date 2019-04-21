var tmi = require('tmi.js')

var options = {
   options: {
      debug: true
},
   connection: {
      cluster: "aws",
      reconnect: true
},
   identity: {
      username: "beachhack_bot",
      password: "oauth:86x30f7gpo4an5imklo42lhbzi2bwn"
},
   channels: ["beachhack_bot"]
};

var client = new tmi.client(options);


client.connect();

client.on('connected', function(address,port){
    client.action("beachhack_bot","REEEEEEEEEEEE TENDIES");
    process.exit(1); 
});
