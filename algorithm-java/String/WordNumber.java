/*
백준 1152번
 */

import java.io.*;

public class WordNumber {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String str = br.readLine().strip();

        if( str.equals(" ") || str.equals(""))
            System.out.println("0");
        else {
            String[] s = str.split(" ");
            System.out.println(s.length);
        }
    }
}
