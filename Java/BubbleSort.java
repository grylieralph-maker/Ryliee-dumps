import java.util.Arrays;
import java.util.ArrayList;

public class BubbleSort{
    public static void main(String args[]){
        ArrayList<Integer> grades = new ArrayList<>(Arrays.asList(90,75,85,60,94,55,83));

        
        for (int i = 0; i<grades.size()-1;i++){
            boolean ok = false;
            for (int j = 0;j<grades.size()-1-i;j++){

                if (grades.get(j+1)>grades.get(j)){
                    int temp = grades.get(j);
                    grades.set(j,grades.get(j+1));

                    grades.set(j+1,temp);
                    ok = true;

                    
                }
                
            }if (!ok){
                    break;}
                
        }

        System.out.println(grades);
    }
    
}