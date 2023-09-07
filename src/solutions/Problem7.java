package solutions;

public class Problem7 implements Problem{

    private boolean isPrime(int num) {
        if (num == 2) return true;
        if (num % 2 == 0) return false;
        for (int i = 3; i <= Math.sqrt(num); i+=2) {
            if (num % i == 0) return false;
        }
        return true;
    }


    @Override
    public void solution() {
        int count = 1;
        int num = 1;
        while (count < 10001) {
            num += 2;
            if (isPrime(num)) count++;
        }
        System.out.println(num);
    }
}
