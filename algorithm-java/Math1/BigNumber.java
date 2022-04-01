/*
백준 10757
 */

import java.io.*;

public class BigNumber {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] str = br.readLine().split(" ");
        int i ;
        String big = str[0].length() < str[1].length() ? str[1] : str[0];
        String small = str[0].length() < str[1].length() ? str[0] : str[1];
        int diff = big.length() - small.length();
        for (i = 0; i< diff; i++)
            small = "0".concat(small);
        int plus = 0;
        String res = "";
        for(i = big.length()-1; i >= 0 ; i--  ){
            int a = small.charAt(i) - '0';
            int b = big.charAt(i) - '0';
            int temp = a + b + plus;
            plus = temp /10;
            res = Integer.toString(temp % 10).concat(res);
        }
        if(plus != 0)
            res = Integer.toString(plus).concat(res);
        System.out.println(res);

    }
}
