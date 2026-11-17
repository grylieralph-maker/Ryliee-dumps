import java.util.Scanner;
public class Main{
    public static void main(String[]args){
        Scanner input = new Scanner(System.in);
        System.out.println("===== STUDENT INFO =====\n");
        System.out.print("Enter your full name: ");
        String name = input.nextLine();
        System.out.print("Enter your age: ");
        int age = input.nextInt();
        System.out.print("Enter your course: ");
        String course = input.next();
        System.out.print("Enter you gpa: ");
        double gpa = input.nextDouble();
        System.out.print("Currently enrolled? ");
        boolean enrolled = input.nextBoolean();

        System.out.println("\n===== STUDENT PROFILE =====");
        System.out.println("Name: "+name);
        System.out.println("Age: "+ age);
        System.out.println("Course: "+ course);
        System.out.println("GPA: "+ gpa);
        System.out.println("Enrolled: "+enrolled);
        
    }
}