function invalid_key(){
a = document.getElementById('id').value
if(typeof a == int){
        window.open("index.html", "_blank");
    }
}
function search() {
    var search_key = document.getElementById('input_id').value;
    let link = "https://0v0g9g.deta.dev/search/1";
    window.open(link)
}