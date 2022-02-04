/*
백준 1011번
 */

import java.io.*;
public class AlphaCentauri {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int caseNum = Integer.parseInt(br.readLine());

        for (int i = 0; i < caseNum; i++) {
            String[] str = br.readLine().split(" ");
            int distance = Integer.parseInt(str[1]) - Integer.parseInt(str[0]);
            int res;
            int max = (int)Math.sqrt(distance);

            if (max == Math.sqrt(distance)) {
                res = max * 2 - 1;
            } else if (distance <= max*(max+1)) {
                res = max * 2;
            } else {
                res = max * 2 + 1;
            }
            System.out.println(res);
        }
    }
}