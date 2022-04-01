/*
백준 1002번
 */

import java.util.Scanner;

public class Turret {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int caseNum = sc.nextInt();

        for (int i = 0; i < caseNum; i++) {
            int x1 = sc.nextInt();
            int y1 = sc.nextInt();
            int r1 = sc.nextInt();
            int x2 = sc.nextInt();
            int y2 = sc.nextInt();
            int r2 = sc.nextInt();

            double distance = Math.sqrt(Math.pow(x1-x2, 2)+Math.pow(y1-y2,2));
            if (distance == 0) {
                if (r1 == r2) {
                    System.out.println(-1);
                } else {
                    System.out.println(0);
                }
            } else if (distance == Math.abs(r2 - r1) || distance == r2 + r1) {
                System.out.println(1);
            } else if (distance > r1 + r2 || distance < Math.abs(r2-r1)) {
                System.out.println(0);
            } else{
                System.out.println(2);
            }
        }
    }
}
