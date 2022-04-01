/*
백준 2775번
 */

import java.io.*;

public class Apartment {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int testCase = Integer.parseInt(br.readLine());

        for(int i = 0; i<testCase; i++){
            int k = Integer.parseInt(br.readLine());
            int n = Integer.parseInt(br.readLine());
            int total = getNum(k, n);

            System.out.println(total);

        }
    }

    static int getNum(int k, int n){
        if(n == 1)
            return 1;
        if(k == 1)
            return n*(n+1)/2;
        else
            return getNum(k,n-1) + getNum(k-1, n);
    }
}
