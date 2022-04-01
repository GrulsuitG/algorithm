/*
백준 11650번
 */

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class PointSort {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        ArrayList<Point> arr = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            Point temp = new Point();
            temp.x = sc.nextInt();
            temp.y = sc.nextInt();

            arr.add(temp);
        }

        Collections.sort(arr);

        for (int i = 0; i < N; i++) {
            System.out.println(arr.get(i));
        }
    }

    static class Point implements Comparable<Point> {
        int x;
        int y;

        @Override
        public int compareTo(Point o) {
            if (this.x < o.x) {
                return -1;
            } else if (this.x > o.x) {
                return 1;
            } else{
                if (this.y < o.y) {
                    return -1;
                } else {
                    return 1;
                }
            }
        }

        @Override
        public String toString() {
            return x+ " " + y;
        }
    }
}
