let obj = {
    x: 1,
    y: 2,
}

let obj2 = Object.create(obj) 
// He will create another object that will inherit (inrrered - Herdar) the properties
// Obj2 (inrreRed)

console.log(obj2.x, obj2.y)

// If i change any property of obj, obj2 will change too
obj.y = 3

console.log(obj2.y)

// But if i change any property of obj2, obj don't will change

obj2.y = 5

console.log(obj.y)

// The object that was inherited don't change through (t.roll - Através do ) 'obj2'

// .hasOwnProperty show if the property is of object