const URL = "https://chatapp.collinchiang.repl.co";

document.addEventListener("DOMContentLoaded", ()=>{
    var authSocket = io.connect(URL + "/auth");

    authSocket.on("connect", function() {
        ;
    });

    authSocket.on("message", function(msg) {
        ;
    });

    document.getElementById("loginSubmit").addEventListener("click", function() {
        authSocket.emit("authenticate", {"page": "login.html"});
    });
});