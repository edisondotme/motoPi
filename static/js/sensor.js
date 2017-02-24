
$(function() {
    // Open a websocket on page load, then update the page with "Connected!"
    // Then wait for a websocket message (.onmessage) and then update the page
    // with that data

    // When we're using HTTPS, use WSS too.
    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    // Create a websocket
    // https://192.168.1.9/sensors/light/
    var chatsock = new ReconnectingWebSocket(ws_scheme + '://' + window.location.host + "/sensors/light/");


    chatsock.onopen = function() {
           console.log("Connected!");
           // $ is apparently a jQuery thing
           // updating a div with jQuery: http://stackoverflow.com/questions/7139208/change-content-of-div-jquery
           $('#sensor').text("Connected!");
           chatsock.send("Connected!");
    };

    chatsock.onmessage = function(message) {
        console.log("Received Sock message!");
        console.log(message);
        $('#sensor').text(message.data);
        // $('#sensor').text('this is test');
    };

});