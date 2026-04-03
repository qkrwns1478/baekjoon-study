import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] inputs = br.readLine().split(" ");
        int[] nums = new int[3];
        for (int i = 0; i < 3; i++) {
            nums[i] = Integer.parseInt(inputs[i]);
        }
        Arrays.sort(nums);

        boolean flag = false;
        if (nums[0] == nums[1]) flag = true;
        else if (nums[1] == nums[2]) flag = true;
        else if (nums[0] + nums[1] == nums[2]) flag = true;
        bw.write(flag ? "S" : "N");

        bw.flush();
        bw.close();
        br.close();
    }
}