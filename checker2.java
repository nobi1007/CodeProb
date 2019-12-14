import java.util.*;
class Java4{
    public static void main(String[] args){
        int n;
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        for(int i=0;i<n;i++){
            System.out.print(" ");
        }
        System.out.print("*");
        System.out.println();
        //main -------------------

        int length = n;
        while(length >= 2){
            int leftSide = n+1;
            int temp = leftSide;
            for(int i=0;i<length;i++){
                for(int j=0;j<temp-2;j++){
                    System.out.print(" ");
                }
                for(int j=0;j<(leftSide - temp + 2);j++){
                    System.out.print("*");
                }
                //right-half
                for(int j=0;j<i+1;j++){
                    System.out.print("*");
                }
                temp--;
                System.out.println();
            }
            length--;
        }
        //main -------------------    
        for(int i=0;i<n;i++){
            System.out.print(" ");
        }
        System.out.print("*");
        System.out.println();
        for(int i=0;i<n;i++){
            System.out.print(" ");
        }
        System.out.print("*");
        System.out.println();
        
    }
}