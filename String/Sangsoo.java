/*
백준 2908번
 */

import java.io.*;

public class Sangsoo {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] s =br.readLine().split(" ");
        int[] num = new int[2];

        for(int n = 0; n < s.length; n++) {
            int digit = 1;
            char[] temp = s[n].toCharArray();
            for (int i = 0; i < temp.length; i++){

                num[n] += (temp[i]-48)*digit;
                digit *= 10;
            }
        }
        if (num[0] > num[1])
            System.out.println(num[0]);
        else
            System.out.println(num[1]);
    }
}
