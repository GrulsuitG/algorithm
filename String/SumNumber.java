/*
백준11720
 */
import java.io.*;

public class SumNumber {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int sum = 0;
        int num = Integer.parseInt(br.readLine());
        for(int i = 0; i< num; i++){
            sum+=br.read()-48;
        }

        System.out.println(sum);
    }
}
