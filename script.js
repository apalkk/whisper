function generator(){
let num = Math.random()
output_file = open('sample.json').read()
    output_json = json.loads(output_file)
    key = str(num)
    for (d in output_json){
        if (key in d){
            generator()
        }
    }
document.getElementById("ToBeChanged").innerHTML = num;
}

/*
function detector(num){
    output_file = open('sample.json').read()
    output_json = json.loads(output_file)
    key = str(num)
    for (d in output_json){
        if (key in d){
            generator()
        }
    }
    return(num)
}*/