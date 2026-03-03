import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        Integer[] arr = new Integer[N];
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(arr, Collections.reverseOrder());
        int answer = -1;
        for (int i = 0; i < N-2; i++) {
            if (arr[i] < arr[i+1] + arr[i+2]) {
                answer = arr[i] + arr[i+1] + arr[i+2];
                break;
            }
        }
        System.out.println(answer);
        br.close();
    }
}