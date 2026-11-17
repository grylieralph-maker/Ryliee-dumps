import java.util.Scanner;
public class Main{
    public static void main(String[]args){
        Scanner input = new Scanner(System.in);
        System.out.print("Enter your grade: ");
        double grade = input.nextDouble();

        if (grade > 100){
            System.out.println("Invalid");
        }else if (grade >= 90){
            System.out.println("Excellent");
        }else if (grade >= 80){
            System.out.println("Very Good");
        }else if (grade >= 75){
            System.out.println("Passed");
        }else if (grade >= 0){
            System.out.println("Failed");
        }else{
            System.out.println("Invalid");
        }
        
        
    }
}
