import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");
        int a=Integer.parseInt(s[0]), b=Integer.parseInt(s[1]);
        if(b>=a-1){
            //치즈 개수가 패티 개수 이상인 경우
            System.out.println(2*a-1);
        }else{
            System.out.println(2*b+1);
        }
    }
}