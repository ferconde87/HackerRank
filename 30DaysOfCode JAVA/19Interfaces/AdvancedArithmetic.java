import java.io.*;
import java.util.*;

interface AdvancedArithmetic{
   int divisorSum(int n);
}


//Write your code here
class Calculator implements AdvancedArithmetic{
    public int divisorSum(int n){
        int result = (n != 1) ? n+1 : 1;
        for(int i = 2; i <= n/2; i++){
            if((n % i) == 0){
                result += i;
            }
        }
        return result;
    }
}

