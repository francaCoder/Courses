// Regular expression serves for manipulate strings

/* 
^ = Beginning of Strings. (Inside array - Denail / Outside array - Beginning of Strings)

For exemple:
"<h1>This is an exemple <p>"
*/

let text = "<h1>This is an exemple <p>"
text.match(/^</) ?  console.log(true) : console.log(false) 

/* 
$ - Final of strings. Too serves as|how capture
*/

text.match(/>$/) ?  console.log(true) : console.log(false) 

// If i want do the match/capture with the beggining and with the final of String/tag, i put:

(/(^<).+(>$)/)

/* 
m - multiline
When i want verify the beggining of much strings that are in multilines
<h1>This is an exemple </h1>
<p>This is an exemple </p>
<div>This is an exemple </div>
*/

(/^>/)
