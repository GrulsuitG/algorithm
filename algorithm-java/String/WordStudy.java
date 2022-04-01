/*
백준 1157번
 */

import java.io.*;

public class WordStudy {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String word = br.readLine().toLowerCase();
        int[] alpha = new int[26];
        for(int i =0; i<word.length(); i++){
            char ch = word.charAt(i);
            alpha[(int)ch-97]++;
        }
        int time = 0;
        char res = 'A';
        for(int i=0; i<26; i++){
            if(alpha[i] > time) {
                time = alpha[i];
                res = (char)(i+65);
            }
            else if(alpha[i] == time){
                res = '?';
            }
        }
        System.out.println(res);
    }
}
