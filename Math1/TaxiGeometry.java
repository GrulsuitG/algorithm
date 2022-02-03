/*
백준 3053번
 */

import java.io.*;

public class TaxiGeometry {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int r = Integer.parseInt(br.readLine());

        System.out.printf("%.6f\n", r*r*Math.PI);
        System.out.printf("%.6f\n", 2.0*r*r);
    }
}
