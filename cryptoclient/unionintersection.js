var a = [1,2,3,4]
var b = [4,5,6]
var c = a
var d = []
var check = false
for(var i of b){
    console.log(i)
    check = false
    for(var j of c){
        if (i == j){
            d.push(i)
            check = true
            break
        }
    }
    if(!check){
        c.push(i)
    }
}
console.log("Union is "+c)
console.log("Intersection is "+d);
