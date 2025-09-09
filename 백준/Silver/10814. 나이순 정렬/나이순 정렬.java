import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

class Member implements Comparable<Member> {
    int age;
    int index;
    String name;

    public Member(int age, int index, String name) {
        this.age = age;
        this.index = index;
        this.name = name;
    }

    @Override
    public int compareTo(Member other) {
        int ageComp = Integer.compare(this.age, other.age);
        if (ageComp == 0) {
            return Integer.compare(this.index, other.index);
        }
        return ageComp;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] input = scanner.nextLine().split(" ");
        int n = Integer.parseInt(input[0]);

        ArrayList<Member> arr = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            String[] tmp = scanner.nextLine().split(" ");
            int age = Integer.parseInt(tmp[0]);
            String name = tmp[1];
            arr.add(new Member(age, i, name));
        }

        Collections.sort(arr);
        for (int i = 0; i < n; i++) {
            System.out.println(arr.get(i).age + " " + arr.get(i).name);
        }
        scanner.close();
    }
}