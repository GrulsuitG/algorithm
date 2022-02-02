/*
백준 4153번
 */

import java.io.*;

public class RightTriangle {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            String[] str = br.readLine().split(" ");
            if (str[0].equals("0")) {
                break;
            }
            int a = Integer.parseInt(str[0]);
            int b = Integer.parseInt(str[1]);
            int c = Integer.parseInt(str[2]);

            a = a*a;
            b = b*b;
            c = c*c;
            if (a == b + c || b == a + c || c == a + b) {
                System.out.println("right");
            } else {
                System.out.println("wrong");
            }
        }
    }
}
