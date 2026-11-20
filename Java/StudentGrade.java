import java.util.Scanner;
import java.util.Collections;
import java.util.ArrayList;

public class StudenGra{
    public static void main(String[]args){

        Scanner input = new Scanner(System.in);
        ArrayList<String> names = new ArrayList<>();
        ArrayList<Double> grades = new ArrayList<>();

        while (true){
            System.out.println("(1) Add Students");
            System.out.println("(2) View All");
            System.out.println("(3) Serach Students");
            System.out.println("(4) Update Score");
            System.out.println("(5) Remove Students");
            System.out.println("(6) Display Highest and Lowest");
            System.out.println("(7) Calculate Average");
            System.out.println("(8) Sort Score");
            System.out.println("(9) Exit");

            int choice = input.nextInt();
            input.nextLine();

            switch(choice){
                case 1:{
                    System.out.print("Enter student name: ");
                    String name = input.nextLine();
                    
                    System.out.print("Enter student grade: ");
                    double grade = input.nextDouble();
                    
                    names.add(name);
                    grades.add(grade);

                    
                    break;
                    
                }
                case 2:{
                    for (int i = 0; i < names.size(); i++){
                        System.out.println("Name: "+names.get(i)+"     Grade: "+grades.get(i));
                        
                    }
                    break;
                    
                }
                case 3:{
                    break;
                    
                }
                case 4:{
                    break;
                    
                }
                case 5:{
                    break;
                    
                }
                case 6:{
                    break;
                    
                }
                case 8:{
                    break;
                    
                }
                default:{
                    
                    
                }}

                if (choice == 9){
                    System.out.println("Program finish");
                    break;
                    }
                    
            
        }
    }
}