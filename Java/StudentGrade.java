import java.util.Scanner;
import java.util.Collections;
import java.util.ArrayList;

public class StudentGrade{
    public static void main(String[]args){

        Scanner input = new Scanner(System.in);
        ArrayList<String> name = new ArrayList<>();
        ArrayList<Integer> grade = new ArrayList<>();

        while (true){
            System.out.println("(1) Add Students");
            System.out.println("(2) View All");
            System.out.println("(3) Serach Students");
            System.out.println("(4) Update Score");
            System.out.println("(5) Remove Students");
            System.out.println("(6) Display Highest and Lowest");
            System.out.println("(7) Calculate Average");
            System.out.println("(8) Sort Score");
        }
    }
}