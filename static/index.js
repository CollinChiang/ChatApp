const URL = "http://127.0.0.1:5000";

document.addEventListener("DOMContentLoaded", ()=>{
    var mainSocket = io.connect(URL);

    mainSocket.on("connect", function() {
        console.log("User Connected (Client)");
    });
    
    mainSocket.on("message", function(msg) {
        console.log("Received Message (Client)");
    });

    document.getElementById("sendLogin").addEventListener("click", function() {
        console.log("CLICKED!");
    });
});