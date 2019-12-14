import java.io.*;
class TryPrime
{
    int isPrime(int p)
    {
        int r=0,c=0;
        for(int k=1;k<=p;++k)
        {
            if(p%k==0){++c;}
        }
        if(c==2)r=1;
        return(r);
    }
        
    static BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[]args)throws IOException
    {
        TryPrime ob=new TryPrime();
        System.out.println("Enter number of testcases");
        int tc=Integer.parseInt(br.readLine());
        for(int i=0;i<tc;++i)
        {
            System.out.println("Enter the size of array");
            int n=Integer.parseInt(br.readLine());
            int a[]=new int[n];
            int b[]=new int[n];
            int c[]=new int[n];
            for(int j=0;j<n;++j)
            {
                a[j]=Integer.parseInt(br.readLine());
            }
            
            int l=0,l1=0;
            
            for(int j=0;j<n;++j)
            {
                
                int g=ob.isPrime(a[j]);
                if(g==1)
                {
                    int h=0;
                    for(int f=0;f<l1;++f)
                    {
                        if(b[f]==a[j]){h=1;c[f]=c[f]+1;++l1;}
                    }
                    if(h==0 || j==0){ b[l]=a[j];c[l]=c[l]+1;++l1;}
                    ++l;
                }
                
            }
            int d[]=new int[l];
            int m=0,t=0,pos=0;
            for(int v=0;v<l-1;++v)
            {
                if(c[v]<c[v+1]){t=c[v+1];pos=v;}
            }
            
            d[m]=b[pos];++m;
            for(int v=0;v<l-1;++v)
            {
                if(c[v]==t){d[m]=b[v];++m;}
            }
            
            for(int v=1;v<m;++v)
            {
                System.out.print(d[v]+" ");
            }
            System.out.println();
        }
    }
}