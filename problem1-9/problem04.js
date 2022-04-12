function checkPalindrome(num) {
    return num === num.split('').reverse().join('');
}

let max = 0;

for (let i = 999; i > 100; i--) {
    for (let j = 999; j > 100; j--) {
        let num = i * j;
        if (num > max && checkPalindrome(num.toString())) max = num;
    }
}

console.log(max);