class Student extends Person{
 private int[] testScores;

    /* 
    *   Class Constructor
    *   
    *   @param firstName - A string denoting the Person's first name.
    *   @param lastName - A string denoting the Person's last name.
    *   @param id - An integer denoting the Person's ID number.
    *   @param scores - An array of integers denoting the Person's test scores.
    */
    // Write your constructor hereint
    Student(String firstName, String lastName, int id, int[] scores){
        super(firstName, lastName, id);
        testScores = scores;
    }

    /* 
    *   Method Name: calculate
    *   @return A character denoting the grade.
    */
    // Write your method here
    public char calculate(){
        int sum = 0;
        for(int i = 0; i < testScores.length; i++){
            sum += testScores[i];
        }
        int avg = sum / testScores.length;
        char ans;
        if(avg >= 90)
                ans = 'O';
        else if (avg >= 80)
                ans = 'E';
        else if (avg >= 70)
                ans = 'A';
        else if (avg >= 55)
                ans = 'P';
        else if (avg >= 40)
                ans = 'D';
            else
                ans = 'T';
        
        return ans;
    }
}