import java.util.Scanner;
import java.util.Collections;
import java.util.ArrayList;

public class StudentGrades{
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
                    if (grades.isEmpty()){
                        System.out.println("The list is empty.");
                    }
                    else{
                        
                    System.out.println("===SEARCH STUDENT===");
                    System.out.print("Search student: ");
                    String search = input.nextLine();

                    int index = names.indexOf(search);

                    if (index != -1){
                        System.out.println("Name: "+search);
                        System.out.println("Grade: "+grades.get(index));
                        }
                    else{
                        System.out.println("Student not found!");
                    }}
                    break;
                    
                }
                case 4:{
                    if (grades.isEmpty()){
                        System.out.println("The list is empty");
                    }
                    else{
                    System.out.println("===UPDATE SCORE===");
                    System.out.print("Enter name: ");
                    String update = input.nextLine();

                    int index = names.indexOf(update);

                    if (index != -1){
                        System.out.print("Change: ");
                        double change = input.nextDouble();
                        grades.set(index, change);
                        
                    }
                    else{
                        System.out.println("Student not found!");
                    }}                    
                    break;
                    
                }
                case 5:{
                    if (grades.isEmpty()){
                        System.out.println("The list is empty");
                    }
                    else{
                        
                    
                    System.out.println("===REMOVE STUDENT===");
                    System.out.print("Enter name: ");
                    String rem = input.nextLine();
                    
                    int index = names.indexOf(rem); 

                    if (index != -1){
                        names.remove(index);
                        grades.remove(index);
                        System.out.println(rem+ " has been removed.");
                    }
                    else{
                        System.out.println("Student not found!");
                    }}
                    
                    break;
                    
                }
                case 6:{
                    if (grades.isEmpty()){
                        System.out.println("The list is empty");
                    }

                    else{
                    System.out.println("===HIGHEST AND LOWEST===");

                    int high = grades.indexOf(Collections.max(grades));

                    int low = grades.indexOf(Collections.min(grades));
                    
                    System.out.println("Highest: "+ names.get(high)+", "+grades.get(high));
                    System.out.println("Lowest: "+names.get(low)+", "+grades.get(low));}
                    
                    break;
                    
                }
                case 7:{
                    if (grades.isEmpty()){
                        System.out.println("The list is empty");
                    }

                    else{
                    System.out.println("===AVERAGE===");
                    double total = 0;
                    for (double grade : grades){
                         total += grade;
                        
                    }
                    double ave = total / grades.size();
                    System.out.println("Average: "+ave);}
                    
                    break;
                }
                case 8:{
                    if (grades.size()<=1){
                        System.out.println("Cant sort, not enough students");
                    }
                    else{
                    System.out.println("===SORT===");
                    boolean swapped;
                    for (int i = 0; i < grades.size()-1;i++){
                        swapped = false;
                        for (int j = 0; j < grades.size()-1-i;j++){
                            if (grades.get(j) > grades.get(j +1)){
                                double temp = grades.get(j);
                                grades.set(j, grades.get(j+1));
                                grades.set(j+1,temp);
                         String tempname = names.get(j);
                                names.set(j,names.get(j+1));
                                names.set(j+1,tempname);
                        swapped = true;
                                                    }
                            
                        }if (!swapped){
                        
                    break;}
                    }
                    for (int a = 0; a<grades.size();a++){
                        System.out.println("Name: "+names.get(a)+"  "+grades.get(a));
                    }}
                    break;
                    
                }
                default:{
                    System.out.println("Invalid choice. Try again");
                    
                    
                }}

                if (choice == 9){
                    System.out.println("Program finished");
                    break;
                    }
                    
            
        }
    }
}