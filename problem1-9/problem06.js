let squareSum = 0;

for (let i = 1; i < 101; i++)
    squareSum += i * i;

let sumSquare = 0;

for (let i = 1; i < 101; i++)
    sumSquare += i;

sumSquare = sumSquare * sumSquare;
console.log(sumSquare - squareSum)