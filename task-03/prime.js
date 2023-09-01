const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function isPrime(num){
    if(num <= 1) return false;
    if(num <= 3) return true;
    if(num % 2 === 0 || num % 3 === 0) return false;

    let i = 5;
    while (i * i <= num){
        if(num % i === 0 || num % (i + 2) === 0) return false;
        i += 6;
    }
    return true;
}

rl.question('', num => {
  n = parseInt(num);
  for (let i = 2; i <= n; i++) {
    if (isPrime(i)) {
      rl.output.write(`${i} `);
    }
  }

  rl.close()
});


// node prime.js