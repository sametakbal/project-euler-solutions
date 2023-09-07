package solutions;

public class Problem3 implements Problem {
    @Override
    public void solution() {
        long num = 600851475143L;
        long div = 2;
        while (num > 1) {
            if (num % div == 0) {
                num /= div;
            } else {
                div += 1;
            }
        }
        System.out.println(div);
    }
}
