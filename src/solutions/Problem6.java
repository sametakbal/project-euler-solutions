package solutions;

public class Problem6 implements Problem{
    @Override
    public void solution() {
        int sumOfSquares = 0;
        int squareOfSum = 0;
        for (int i = 1; i <= 100; i++) {
            sumOfSquares += i * i;
            squareOfSum += i;
        }
        squareOfSum *= squareOfSum;
        System.out.println(squareOfSum - sumOfSquares);
    }
}
