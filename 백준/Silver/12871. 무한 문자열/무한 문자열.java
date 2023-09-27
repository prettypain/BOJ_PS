import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String a = br.readLine(), b = br.readLine();
        boolean is = false;
        String sa="",sb="";
        int mul_len = a.length()*b.length();
        
        for(int i=0; sa.length()<mul_len; i++) sa+=a;
        for(int i=0; sb.length()<mul_len; i++) sb+=b;

        if(sa.equals(sb)) is=true;

        System.out.println(is==true?1:0);
    }
}