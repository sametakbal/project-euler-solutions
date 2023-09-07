package solutions;

public class Problem1 implements Problem{

    // https://projecteuler.net/problem=1

    public void solution() {
        int sum = 0;
        for (int i = 0; i < 1000; i++) {
            if ((i%3 == 0) || (i%5 == 0)) {
                sum += i;
            }
        }
        System.out.println(sum);
    }
}
