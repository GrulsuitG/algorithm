/*
백준 1065
 */

import java.io.*;

public class SelfNumber{

    int d(int num){
        int sum = num;
        while( num != 0){
            sum += num%10;
            num /= 10;
        }
        return sum;
    }

    public static void main(String[] args) throws IOException {
        int res;
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int[] arr = new int[10001];
        SelfNumber s = new SelfNumber();

        for(int i = 1; i<10000; i++){
            res = s.d(i);
            try {
                arr[res] = 1;
            }catch(Exception e){
            }
        }

        for(int i = 1; i<10000; i++){
            if (arr[i] == 0)
//                bw.write(Integer.toString(i));
                System.out.println(i);
        }
    }


}
