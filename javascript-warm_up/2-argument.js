#!usr/bin/node

const argCount = process.argv.length -2;

if (argCount === 0) {
    console.log('No Argument');
} else if (argCount === 1) {
    console.log('Argument found');
} else {
    console.log('Arguments found');
}
