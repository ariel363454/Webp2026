var dataUrl = "https://www.flickr.com/services/feeds/photos_public.gne?format=json&nojsoncallback=1";

function getimg() {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', dataUrl, true);
    xhr.send();

    xhr.onload = function() {
        if (this.status == 200) {
            var data = JSON.parse(this.responseText);
            add_new_img(data.items);
        }
    };
}

function add_new_img(dataset) {
    var gal = document.getElementById("gallery"); 
    gal.innerHTML = "";

    dataset.slice(0, 6).forEach(function(item) {
        var img = document.createElement("img");
        
        img.setAttribute("src", item.media.m);
        
        gal.appendChild(img);
    });
}
