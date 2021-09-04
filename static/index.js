const URL = "https://chatapp.collinchiang.repl.co";

document.addEventListener("DOMContentLoaded", ()=>{
    var mainSocket = io.connect(URL);

    mainSocket.on("connect", function() {
        console.log("User Connected (Client)");
    });
    
    mainSocket.on("message", function(msg) {
        console.log("Received Message (Client)");
    });
});