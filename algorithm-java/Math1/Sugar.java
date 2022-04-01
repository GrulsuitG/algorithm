/*
백준 2839
 */

import java.io.*;

public class Sugar {
    public static void main(String[] args) throws IOException {
        solve2();
    }

    static void solve1() throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        int five = n/5 ;
        int three = (n%5)/3;
        int remainder = n%5%3;
        while (true){
            if(five*5 + three*3 == n) {
                System.out.println(five + three);
                break;
            }
            five--;
            three += (remainder+5) /3;
            remainder = (remainder+5) %3;
            if(five == -1)
                break;
        }

        if(five == -1)
            System.out.println((-1));
    }

    static void solve2() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        /*
        1  2  3  4  5  6  7  8  9  10
        -1 -1 1 -1  1 2 -1  2  3  2

        11 12 13 14 15 16 17 18 19 20
        3  4  3  4  3  4  5  4  4  4
         */

        if( n == 4 || n== 7)
            System.out.println(-1);
        else if (n % 5 == 0)
            System.out.println(n/5);
        else if (n % 5 == 1 || n% 5 == 3)
            System.out.println((n/5) + 1);
        else if( n % 5 ==2 || n% 5 == 4)
            System.out.println((n/5) +2 );
    }
}
