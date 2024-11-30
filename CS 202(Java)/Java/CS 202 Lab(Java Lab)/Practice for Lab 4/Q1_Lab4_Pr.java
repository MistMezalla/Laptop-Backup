import java.util.*;

public class Q1_Lab4_Pr {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter the number of test cases: ");
        int n = sc.nextInt();

        int[] test_cases_size = new int[n];
        System.out.println("Enter the sizes of each test case: ");
        for (int i = 0; i < n; i++) {
            test_cases_size[i] = sc.nextInt();
        }

        int[][] test_cases = new int[n][];
        System.out.println("Enter the values for each test case: ");
        for (int i = 0; i < n; i++) {
            test_cases[i] = new int[test_cases_size[i]];
            for (int j = 0; j < test_cases_size[i]; j++) {
                test_cases[i][j] = sc.nextInt();
            }
        }

        int total_even = 0;
        int total_odd = 0;

        for (int i = 0; i < n; i++) {
            int[] result = even_odd(test_cases[i]);
            int even_count = result[0];
            int odd_count = result[1];

            System.out.println("Test Case " + (i + 1) + ":");
            System.out.println("Even numbers: " + even_count);
            System.out.println("Odd numbers: " + odd_count);


            total_even += even_count;
            total_odd += odd_count;
        }


        System.out.println("Overall Even numbers: " + total_even);
        System.out.println("Overall Odd numbers: " + total_odd);
    }


    static int[] even_odd(int[] nums) {
        int cnt_even = 0;
        for (int num : nums) {
            if ((num & 1) == 0) {
                cnt_even += 1;
            }
        }
        int cnt_odd = nums.length - cnt_even;
        return new int[]{cnt_even, cnt_odd};
    }
}
