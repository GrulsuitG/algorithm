/*
백준 1316번
 */

import java.io.*;
import java.util.ArrayList;

public class GroupWordChecker {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int num = Integer.parseInt(br.readLine());
        int total = 0;
        for (int i = 0; i < num; i++) {
            ArrayList<Character> list = new ArrayList<>();
            char[] str = br.readLine().toCharArray();
            boolean isGroup = true;

            for (int j = 0; j < str.length; j++) {
                if (list.contains(str[j])) {
                    if (str[j - 1] != str[j]) {
                        isGroup = false;
                        break;
                    }
                }else {
                    list.add(str[j]);
                }
            }
            if (isGroup)
                total++;
        }

        System.out.println(total);

    }
}

