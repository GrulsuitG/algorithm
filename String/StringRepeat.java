/*
백준 2675번
 */
import java.io.*;

public class StringRepeat {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int times = Integer.parseInt(br.readLine());
        for(int i =0; i<times; i++) {
            String[] list = br.readLine().split(" ");
            String word = list[1];
            int repeat = Integer.parseInt(list[0]);
            for(int j = 0; j<word.length(); j++){
                for(int k=0; k<repeat; k++)
                    System.out.print(word.charAt(j));
            }
            System.out.println();
        }
    }
}
