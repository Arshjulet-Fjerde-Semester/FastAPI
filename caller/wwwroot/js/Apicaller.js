

// This function should get a Message from the API
// and convert the message into a readable format, which can be presented in the view
function sendMessage(){
    $.ajax({
        url: "http://127.0.0.1:8000/files",
        type: "GET",
        success: function (result) {
            alert("success");
            console.log(result);
            var arraybuf = base64ToArrayBuffer(result);
            var blob = new Blob([arraybuf], {type: "application/pdf"});
            console.log(blob);
            var newelement = window.URL.createObjectURL(blob);
            document.getElementById("WebGl").src = newelement;
        },
        error: function (error) {
            alert("error");
            console.log(error);
        }
    })

}



// function sendMessage() {
//         var ws = new WebSocket("ws://localhost:8000/ws");
//         ws.onmessage = function(event) {
//             base64 = blobToBase64(event.data)
//             var arraybuf = base64ToArrayBuffer(base64);
//             console.log(arraybuf);
//             var blob = new Blob(arraybuf, {type: "application/pdf"});
//             var newelement = window.URL.createObjectURL(blob);
//             document.getElementById("WebGl").src = newelement; 
            
//         };
// };


//This function converts a blob to a base64 string, to get the needed data from the blob
function blobToBase64(blob) {
    return new Promise((resolve, _) => {
      const reader = new FileReader();
      reader.onloadend = () => resolve(reader.result);
      reader.readAsDataURL(blob);
    });
  }

//This function takes a base64 string and adds it to a Uint8array, after that is done it should return the array
function base64ToArrayBuffer(base64) {
    var binaryString = window.atob(base64);
    var binaryLen = binaryString.length;
    var bytes = new Uint8Array(binaryLen);
    for (var i = 0; i < binaryLen; i++) {
        var ascii = binaryString.charCodeAt(i);
        bytes[i] = ascii;
    }
    return bytes;
}