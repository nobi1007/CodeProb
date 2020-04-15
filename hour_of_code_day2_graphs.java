import java.lang.*;
import java.io.*;
import java.util.*;

class hoc2graphs{
    public static void main(String args[])throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line1[] = br.readLine().split("\\s+");
        int n = Integer.parseInt(line1[0]);
        int d = Integer.parseInt(line1[1]);

        int mat[][] = new int[n][n];
        int visited[] = new int[n];
        int label = 0;
        for (int i=0;i<d;i++){
            String linex[] = br.readLine().split("\\s+");
            int x = Integer.parseInt(linex[0]);
            int y = Integer.parseInt(linex[1]);
            mat[x][y] = 1;
            mat[y][x] = 1;
            label = x;
        }
        int root = label;
        Stack<Integer> stack = new Stack<Integer>();
        stack.push(root);
        while(!stack.isEmpty()){
            root = stack.pop();
            for(int j=0;j<n;j++){
                if(mat[root][j] == 1 && visited[j]==0){
                    stack.push(j);
                    visited[j] = 1;
                }
            }
        }
        boolean check = true;
        for(int x:visited){
            if(x==0){
                check = false;
                break;
            }
        }
        if(check){
            System.out.println("YES");
        }
        else{
            System.out.println("NO");
        }

    }
}