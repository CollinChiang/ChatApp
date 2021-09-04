const URL = "http://127.0.0.1:5000";

document.addEventListener("DOMContentLoaded", ()=>{
    var authSocket = io.connect(URL + "/auth");

    authSocket.on("connect", function() {
        ;
    });

    authSocket.on("message", function(msg) {
        ;
    });

    document.getElementById("loginSubmit").addEventListener("click", function() {
        alert("Clicked!");
        authSocket.emit("authenticate", {"set1": "data1","set2": "data2"});
        console.log("Success");
    });
});