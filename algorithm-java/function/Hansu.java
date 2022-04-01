/*
백준 4673
 */


import java.io.*;

public class Hansu {
    public static boolean isAP(int n){
        int[] arr = new int[4];
        for(int i = 0; i<4; i++){
            arr[i] = n%10;
            n = n/10;
        }
        int digit = 0;
        for(int i = 3; i>=0; i--){
            if(arr[i] != 0) {
                digit = i;
                break;
            }
        }

        int diff = arr[1] - arr[0];
        for(int i = 0; i<digit; i++){
            int temp = arr[i+1] - arr[i];
            if (diff != temp)
                return false;
        }
        return true;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int num = Integer.parseInt(br.readLine());
        int cnt = 0;
        for(int i =1; i<= num; i++)
            if(isAP(i))
                cnt++;

        System.out.println(cnt);
    }
}
