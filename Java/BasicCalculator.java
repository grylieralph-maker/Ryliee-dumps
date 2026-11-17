import java.util.Scanner;

public class BasicCalculator{
    public static void main(String[]args){

        Scanner input = new Scanner(System.in);
        System.out.print("Enter first number: ");
        double num1 = input.nextDouble();
        System.out.print("Enter second number: ");
        double num2 = input.nextDouble();
        System.out.println("Operator: (+) (-) (x) (÷)");
        System.out.print("Enter the operator: ");
        char operation = input.next().charAt(0);

        switch (operation){
            case '+':{
                System.out.println(num1 + " + " + num2 + " =  " + (num1 + num2));
                break;
                
            }
            case '-':{
                System.out.println(num1 + " - " + num2 + " = " + (num1 - num2));
                break;
            }
            case 'x':{
                System.out.println(num1 +" x "+num2+" = "+(num1 * num2));
                break;
            }
            case '÷':{
                if (num2 == 0){
                    System.out.println("Cannot divide by zero!");
                }
                else{
                    System.out.println(num1+" ÷ "+num2+" = "+(num1 / num2));
                }break;
            }
            default:{
                System.out.println("Invalid operator!");
            } 
        }
        
    }
    
}
