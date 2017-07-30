import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();
        for(int k = 0; k < n; k++){
            String s = sc.nextLine();
            int length = s.length();
            char[] cs = s.toCharArray();
            for(int i = 0; i < length; i+=2){
                System.out.print(cs[i]);
            }
            System.out.print(" ");
            for(int i = 1; i < length; i+=2){
                System.out.print(cs[i]);
            }
            System.out.println();
        }
    }
}