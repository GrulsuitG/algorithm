/*
백준 1181번
 */


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class WordSort {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        ArrayList<String> arr = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            String str = br.readLine();
            arr.add(str);
        }

        arr.sort((e1, e2) -> {
            if (e1.length() > e2.length()) {
                return 1;
            } else if (e1.length() < e2.length()) {
                return -1;
            } else {
                return e1.compareTo(e2);
            }
        });
        for (int i = 1; i <= N; i++) {
            if (i == N || !arr.get(i - 1).equals(arr.get(i))) {
                System.out.println(arr.get(i-1));
            }
        }

    }

}
