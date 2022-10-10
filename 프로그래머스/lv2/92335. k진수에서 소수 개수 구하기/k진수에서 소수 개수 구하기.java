class Solution {
    public static String convert(int n, int k) {
        int tmp = n;
        String convert_num = "";

        while(true) {
            if (tmp < k) {
                convert_num = tmp + convert_num;
                break;
            }
            int leaves = tmp % k;
            tmp = tmp / k;
            convert_num = leaves + convert_num;
        }
        return convert_num;
    }

    public static boolean is_prime(long n) {
        if (n == 1)
            return false;
//        System.out.println(Math.sqrt(n));
        for(long i = 2; i < Math.floor(Math.sqrt(n)) + 1; i++) {
            if (n % i == 0)
                return false;
        }
        return true;
    }

    public static int solution(int n, int k) {
        int answer = 0;
        String number = convert(n, k);
        String[] arr = number.split("0");
        for (String a: arr) {
            if (!a.isEmpty() && is_prime(Long.parseLong(a))) {
                answer += 1;
            }
        }

        return answer;
    }
}