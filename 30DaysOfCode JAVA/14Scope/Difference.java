import java.util.*;

class Difference {
   private int[] elements;
   public int maximumDifference;
   // Add your code here
   Difference(int[] elements){
       this.elements = elements;
   }

   void computeDifference(){
       IntSummaryStatistics stat = Arrays.stream(elements).summaryStatistics();
       int min = stat.getMin();
       int max = stat.getMax();
       maximumDifference = max - min;
   }
}// End of Difference class