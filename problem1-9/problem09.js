for (let i = 0; i < 1000; i++) {
    for (let j = 0; j < 1000; j++) {
        let temp = (i ** 2) + (j ** 2);
        if (i + j + (temp ** (0.5)) === 1000) {
            console.log(i * j * (temp ** (0.5)))
        }
    }
}