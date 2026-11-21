import java.util.Scanner;
import java.util.Collections;
import java.util.ArrayList;

public class StudenGrades{
    public static void main(String[]args){

        Scanner input = new Scanner(System.in);
        ArrayList<String> names = new ArrayList<>();
        ArrayList<Double> grades = new ArrayList<>();

        while (true){
            System.out.println("(1) Add Students");
            System.out.println("(2) View All");
            System.out.println("(3) Search Students");
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
                    System.out.println("===ADD STUDENT===");
                    System.out.print("Enter student name: ");
                    String name = input.nextLine();
                    
                    System.out.print("Enter student grade: ");
                    double grade = input.nextDouble();
                    
                    names.add(name);
                    grades.add(grade);

                    
                    break;
                    
                }
                case 2:{
                    System.out.println("===SHOW ALL===");
                    for (int i = 0; i < names.size(); i++){
                        System.out.println("Name: "+names.get(i));
                        System.out.println("Grade: "+grades.get(i));
                        System.out.println();
                        
                    }
                    break;
                    
                }
                case 3:{
                    System.out.println("===SEARCH STUDENT===");
                    System.out.print("Search student: ");
                    String search = input.nextLine();

                    int index = names.indexOf(search);

                    if (index != -1){
                        System.out.println("Name: "+search);
                        System.out.println("Grade: "+grades.get(index));
                    }
                    break;
                    
                }
                case 4:{
                    System.out.println("===UPDATE SCORE===");
                    System.out.print("Enter name: ");
                    String update = input.nextLine();

                    int index = names.indexOf(update);

                    if (index != -1){
                        System.out.print("Change: ");
                        double change = input.nextDouble();
                        grades.set(index, change);
                        
                    }                    
                    break;
                    
                }
                case 5:{
                    
                    break;
                    
                }
                case 6:{
                    break;
                    
                }
                case 7:{
                    
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