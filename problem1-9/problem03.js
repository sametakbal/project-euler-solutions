let num = 600851475143;
div = 2
while (num > 1) {
    if (num % div === 0)
        num /= div
    else
        div += 1
}
console.log(div)