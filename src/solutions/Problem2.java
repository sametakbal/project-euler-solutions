package solutions;

public class Problem2 implements Problem {
    @Override
    public void solution() {
        int first = 1;
        int second = 1;
        int total = 0;
        int term = 2;

        while (term < 4000000) {
            term = first + second;
            if (term % 2 == 0) total += term;
            first = second;
            second = term;
        }
        System.out.println(total);
    }
}
