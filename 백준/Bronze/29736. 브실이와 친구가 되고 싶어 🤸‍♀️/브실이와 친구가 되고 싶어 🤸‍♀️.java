import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");
        int a=Integer.parseInt(s[0]), b=Integer.parseInt(s[1]),c=0;
        s = br.readLine().split(" ");
        int k=Integer.parseInt(s[0]), x=Integer.parseInt(s[1]);
        
        for(int i=a; i<=b; i++){
            if(i>=k-x && i<=k+x) c++;
        }
        
        System.out.println(c>0 ? c : "IMPOSSIBLE");

        br.close();
    }
}