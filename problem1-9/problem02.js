let first = 1;
let second = 1;
let total = 0;
let term = 2;

while (term < 4000000) {
    term = first + second;
    if (term % 2 === 0) total += term;
    first = second;
    second = term;
}
console.log(total);