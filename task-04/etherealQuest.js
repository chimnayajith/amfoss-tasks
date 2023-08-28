// cp-praveshan-2023/ethereal-quest

const readline = require('readline');

//creating interface for input and output
const input = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const sum = [0, 0, 0];
let t = 0; //test case count 
let i = 0; //current test case

//entering the number of test cases
input.question('', num => {
  t = parseInt(num);

  if (1 <= t && t <= 100) {
    //inputing values seperated by ' '
    input.on('line', line => {
      const [x, y, z] = line.split(' ').map(Number);

      if (!(-100 <= x && x <= 100 && -100 <= y && y <= 100 && -100 <= z && z <= 100)) {
        input.close();
        return;
      }

      // adding values to the existing sum
      sum[0] += x;
      sum[1] += y;
      sum[2] += z;

      //next test case
      i++;

      if (i === t) {
        input.close();
      }
    });

    input.on('close', () => {
      if (sum.every(each=> each === 0)) {
        console.log('YES');
      } else {
        console.log('NO');
      }
    });
  }
});
