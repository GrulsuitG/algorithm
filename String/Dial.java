/*
백준 5622
 */

import java.io.*;

public class Dial {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] str = br.readLine().split("");
        int time = 0;

        for(String s : str){
            if(s.charAt(0) == '1')
                time += 2;
            else if (s.charAt(0) >= 'A' && s.charAt(0) <= 'C')
                time += 3;
            else if (s.charAt(0) >= 'D' && s.charAt(0) <= 'F')
                time += 4;
            else if (s.charAt(0) >= 'G' && s.charAt(0) <= 'I')
                time += 5;
            else if (s.charAt(0) >= 'J' && s.charAt(0) <= 'L')
                time += 6;
            else if (s.charAt(0) >= 'M' && s.charAt(0) <= 'O')
                time += 7;
            else if (s.charAt(0) >= 'P' && s.charAt(0) <= 'S')
                time += 8;
            else if (s.charAt(0) >= 'T' && s.charAt(0) <= 'V')
                time += 9;
            else if (s.charAt(0) >= 'W' && s.charAt(0) <= 'Z')
                time += 10;
            else
                time += 11;
        }

        System.out.println(time);
    }
}
