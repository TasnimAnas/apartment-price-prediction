function onPageLoad() {
    var url = "/api/get_location"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
    $.get(url, function (data, status) {
        if (data) {
            var locations = data.locations;
            var uiLocations = document.getElementById("location");
            $('#location').empty();
            for(var i in locations) {
                var opt = new Option( locations[i], locations[i]);
                $('#location').append(opt);
            }
        }
    });
}
  
function getEstimatedPrice() {
    document.getElementById("sqft").checkValidity()
    var sqft = Number(document.getElementById("sqft").value);
  var bhk = Number(document.getElementById("bhk").value);
  var bathrooms = Number(document.getElementById("bath").value);
    var location = document.getElementById("location").value;
    var balcony = Number(document.getElementById("balcony").value);
    if (sqft && bhk && bathrooms && location && balcony) {
        var url = "/api/get_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards

        $.post(url, {
            sqft: sqft,
            bhk: bhk,
            bath: bathrooms,
            balcony: balcony,
            location: location
        },function(data, status) {
            document.getElementById("price").innerText = `${data.price} Lakhs`
        });
    }
}

function Reset() {
    document.getElementById("sqft").value = null
    document.getElementById("bhk").value = null
    document.getElementById("bath").value = null
    document.getElementById("location").value = null
    document.getElementById("balcony").value = null
    document.getElementById("price").innerText = null
}
  
  window.onload = onPageLoad;