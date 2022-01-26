/*
백준 1712
손익분기점
 */

import java.io.*;

public class BEP {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] str = br.readLine().split(" ");
        long[] num = new long[3];
        long time;
        for(int i =0; i<3; i++){
            num[i] = Integer.parseInt(str[i]);
        }

        if(num[2] - num[1] <= 0)
            System.out.println("-1");
        else{
            time = num[0] / (num[2] - num[1]);
            System.out.println(time+1);
        }

    }
}
