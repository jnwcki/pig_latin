var vowels = ['a', 'e', 'i', 'o', 'u'];

var firstName = prompt("What is your first name?");

if ( vowels.indexOf(firstName[0].toLowerCase()) >= 0 ) {
  document.write("<h3>Your pig latin first name is: " + firstName[1] + firstName.slice(2) + "say</h3>");
} else {
  document.write("<h3>Your pig latin first name is: " + firstName[1] + firstName.slice(2) + firstName[0] + "ay</h3>")
}
