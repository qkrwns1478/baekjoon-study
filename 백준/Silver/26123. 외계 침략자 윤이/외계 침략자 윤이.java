import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int D = Integer.parseInt(st.nextToken());
        int[] nums = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(nums);
        long answer = 0;
        int cnt = 1;
        for (int i = N-1; i > 0; i--) {
            if (D <= 0)
                break;
            else if (nums[i] == nums[i-1])
                cnt++;
            else {
                int diff = nums[i] - nums[i-1];
                if (D >= diff) {
                    answer += (long) diff * cnt;
                    D -= diff;
                    cnt++;
                } else {
                    answer += (long) D * cnt;
                    D = 0;
                }
            }
        }
        if (D > 0 && nums[0] > 0) {
            int min = Math.min(D, nums[0]);
            answer += (long) min * N;
        }
        System.out.println(answer);
    }
}