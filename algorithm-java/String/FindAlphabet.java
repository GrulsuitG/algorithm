/*
백준 10809
 */
import java.io.*;

public class FindAlphabet {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String word = br.readLine();
        int len = word.length();
        for(int i='a'; i<='z'; i++){
            System.out.print(word.indexOf(i)+" ");
        }
    }
}
