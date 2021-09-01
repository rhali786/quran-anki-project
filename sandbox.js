const { convertArrayToCSV } = require('convert-array-to-csv');
const converter = require('convert-array-to-csv');
 
const header = ['number', 'first', 'last', 'handle'];
const dataArrays = [
  [1, 'Mark', 'Otto', '@mdo'],
  [2, 'Jacob', 'Thornton', '@fat'],
  [3, 'Larry', 'the Bird', '@twitter'],
];
 
/*
  const csvFromArrayOfObjects  = 'number,first,last,handle\n1,Mark,Otto,@mdo\n2,Jacob,Thornton,@fat\n3,Larry,the Bird,@twitter\n';
*/

 
/*
  const csvFromArrayOfArrays  = 'number;first;last;handle\n1;Mark;Otto;@mdo\n2;Jacob;Thornton;@fat\n3;Larry;the Bird;@twitter\n';
*/
const csvFromArrayOfArrays = convertArrayToCSV(dataArrays, {
  header,
  separator: ';'
});
console.log(csvFromArrayOfArrays)