function pdftest(){


    $.ajax({
        url: "https://api.coindesk.com/v1/bpi/currentprice.json",
        type: "GET",
        success: function (result) {
            alert("success");
            console.log(result);
        },
        error: function (error) {
            alert("error");
            console.log(error);
        }
    }
    )

}
