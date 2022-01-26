/*
백준 2292번
 */

import java.io.*;

public class Honeycomb {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int num = Integer.parseInt(br.readLine());

        int time = 1;
        while(true) {
            if(3 * time * time - 3 * time + 1 >= num)
                break;
            time++;
        }
        System.out.println(time);
    }
}
