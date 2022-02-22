/*
백준 10814번
 */

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class AgeSort {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        ArrayList<Member> arr = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            arr.add(new Member(i, sc.nextInt(), sc.next()));
        }

        Collections.sort(arr);

        for (Member member : arr) {
            System.out.println(member);
        }
    }

    static class Member implements Comparable<Member>{
        int index;
        int age;
        String name;

        public Member(int index, int age, String name) {
            this.index = index;
            this.age = age;
            this.name = name;
        }

        @Override
        public int compareTo(Member o) {
            if (age > o.age) {
                return 1;
            } else if (age < o.age) {
                return -1;
            } else {
                if (index > o.index) {
                    return 1;
                } else
                    return -1;
            }
        }

        @Override
        public String toString() {
            return age + " " + name;
        }
    }
}
