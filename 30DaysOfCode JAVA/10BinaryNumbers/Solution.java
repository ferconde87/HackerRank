import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int cur = 0;
        int max = 0;
        while(n > 0){
            if(n%2 == 1){
                cur++;
                max = Math.max(max, cur);
            }else{
                cur = 0;
            }
            n /= 2;
        }
        System.out.println(max);       
    }
}