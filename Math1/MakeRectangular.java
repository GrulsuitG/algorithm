/*
백준 3009번
 */

import java.util.Scanner;

public class MakeRectangular {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] point = new int[6];

        for (int i = 0; i < 6; i++) {
            point[i] = sc.nextInt();
        }
        int x = point[0], y = point[1];
        if (x == point[2]) {
            x = point[4];
        } else if (x == point[4]) {
            x = point[2];
        }
        if (y == point[3]) {
            y = point[5];
        } else if (y == point[5]) {
            y = point[3];
        }
        System.out.println(x + " " + y);



    }
}
