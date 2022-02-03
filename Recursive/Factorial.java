/*
백준 10872번
*/
import java.io.*;

public class Factorial {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        int res = Calc(n);
        System.out.println(res);
    }

    private static int Calc(int n) {
        if(n <2)
            return 1;
        else
            return n * Calc(n-1);
    }
}
