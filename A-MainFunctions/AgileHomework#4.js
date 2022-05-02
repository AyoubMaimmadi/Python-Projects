// Ayoub Maimmadi: 76678

// name check function using JavaScript
// check that a name only includes alphabetical characters, -, or
// a single quote. Names must be between 2 and 40 characters long.
// Quoted strings and -- are not allowed.
const nameCheck = (name) => {
  var nameRegex = /^[a-zA-Z-']{2,40}$/
  if (name.includes('--')) {
    return false
  }
  return nameRegex.test(name)
}

// Stored All names ti be tested in an arr
names = [
  '',
  'a',
  'Ayoub',
  'SommerVill',
  `Thisis'malicious`,
  `S`,
  `C-3PO`,
  `--badcode`,
  `Washington-Willson`,
  `Sommer_vill`,
  `'Sommer_vill`,
  `0'Reilly`,
  `Sx`,
  `0 Reilly`,
  '',
  'a',
  'Ayoub',
  'SommerVill',
  `Thisis'malicious`,
  `S`,
  `C-3PO`,
  `--badcode`,
  `Washington-Willson`,
  `Sommer_vill`,
  `'Sommer_vill`,
  `0'Reilly`,
  `Sx`,
  `0 Reilly`,
]

// Test each name in the array
for (var i = 0; i < names.length; i++) {
  if (!nameCheck(names[i])) {
    console.log(names[i] + '\t is not a valid name.\t\tFAIL')
  } else {
    console.log(names[i] + '\t is a valid name.\t\tok')
  }
}
