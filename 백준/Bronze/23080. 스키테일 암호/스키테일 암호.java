import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int k = Integer.parseInt(br.readLine());
        String s = br.readLine();
        for(int i=0; i<s.length(); i++){
            if(i%k==0) System.out.print(s.charAt(i));
        }
    }
}