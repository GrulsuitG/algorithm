/*
백준 2941번
1. Backward parsing 을 통해 case 를 단순화
2. replace method 를 이용하는 방법

1번 풀이는 인터넷에서 찾아보기 힘든데
2번 코드가 완전 짧아서 좋아 보인다.
 */

import java.io.*;

public class CroatiaAlphabet {
    public static void main(String[] args) throws IOException {
        // 1번
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        char[] str = br.readLine().toCharArray();
        int total = 0;
        for(int i =  str.length-1; i >= 0; i--){
            char c = str[i];
            if( c == '='){
                if (str[i - 1] == 'z') {
                    try{
                        if (str[i - 2] == 'd') {
                            i--;
                        }
                    } catch (Exception e) {
                    }
                }
                i--;
            } else if( c == '-'){
                i--;
            } else if (c == 'j') {
                try {
                    if (str[i - 1] == 'l' || str[i - 1] == 'n')
                        i--;
                } catch (Exception e) {
                }
            }
            total++;
        }
        System.out.println(total);

    }
    //2번
//    public static void main(String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//
//        String str = br.readLine();
//        String[] croatia = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};
//
//        for(String s : croatia){
//            if(str.contains(s))
//                str = str.replace(s, "0");
//        }
//        System.out.println(str.length());
//    }
}
