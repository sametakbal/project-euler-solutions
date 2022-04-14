//Bütün asal sayılar 6n+1 veya 6n-1 kuralına uyar. 2 ve 3 hariç. Köküne kadar bölümüyorsa sayı asaldır.

//All prime numbers follow the 6n+1 or 6n-1 rule. Except 2 and 3. and prime if the number is not divided by until its root

function checkPrime(num) {
    let j = 2;
    while (j <= (num ** (0.5))) {
        if (num % j === 0)
            return false
        j++;
    }
    return true
}

let arr = [];
arr.push(2)
arr.push(3)
let count = 2;
let i = 1;
while (count < 10001) {
    if (checkPrime(i * 6 + 1)) {
        arr.push(i * 6 + 1);
        count++;
    }
    if (checkPrime(i * 6 - 1)) {
        arr.push(i * 6 - 1)
        count++;
    }
    i += 1
}
console.log(arr.pop())