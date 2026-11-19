import java.util.Scanner;

public class Triangle{
    public static void main(String[]args){
        Scanner input = new Scanner(System.in);
        System.out.print("Rows: ");
        int rows = input.nextInt();

        for (int i = 1;i <= rows ;i++){
            for (int spaces = 1;spaces <=rows -i ;spaces ++){
                System.out.print(" ");
            }
            for (int stars = 1; stars <= i *2 - 1; stars++){
                System.out.print("*");
            }
        System.out.println();}
    }
}