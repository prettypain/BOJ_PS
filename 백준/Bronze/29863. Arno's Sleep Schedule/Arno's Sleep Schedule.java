import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int s=Integer.parseInt(br.readLine()), e=Integer.parseInt(br.readLine());
        
        if(s > e){
            System.out.println((24-s) + e);
        }else{
            System.out.println(e-s);
        }
    }
}