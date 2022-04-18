function checkPrime(num) {
    let n = 2;
    while (n <= (num ** (0.5))) {
        if (num % n === 0)
            return false;
        n += 1;
    }
    return true;
}

let total = 5;  // 2,3
let i = 1;
while ((i * 6 + 1) < 2000000) {
    if (checkPrime(i * 6 + 1))
        total += (i * 6 + 1);
    if (checkPrime(i * 6 - 1))
        total += (i * 6 - 1);
    i += 1;
}

console.log(total)