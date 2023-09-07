package solutions;

public class Problem4 implements Problem {

    private boolean isPalindrome(int num) {
        String str = Integer.toString(num);
        int len = str.length();
        for (int i = 0; i < len / 2; i++) {
            if (str.charAt(i) != str.charAt(len - i - 1)) return false;
        }
        return true;
    }

    @Override
    public void solution() {
        int max = 0;
        for (int i = 999; i > 100; i--) {
            for (int j = 999; j > 100; j--) {
                int num = i * j;
                if (num > max && isPalindrome(num)) {
                    max = num;
                }
            }
        }
        System.out.println(max);
    }
}
