function twenty(num) {
    let j = 11;
    let ch = 0;
    while (j <= 20) {
        if (num % j === 0)
            ch += 1;
        j += 1;
    }
    return ch;
}
// 2520*11*13*17*19 first multiplied by prime numbers
i = 116396280
while (twenty(i) !== 10)
    i += 1
console.log(i)