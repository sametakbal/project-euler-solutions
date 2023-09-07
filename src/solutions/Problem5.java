package solutions;

public class Problem5 implements Problem{
    @Override
    public void solution() {
        int num = 20;
        while (true) {
            boolean divisible = true;
            for (int i = 1; i <= 20; i++) {
                if (num % i != 0) {
                    divisible = false;
                    break;
                }
            }
            if (divisible) break;
            num++;
        }
        System.out.println(num);
    }
}
