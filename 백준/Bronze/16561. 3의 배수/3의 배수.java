/*
n을 3개의 3의 배수로 분리했을 때 3개의 수를 i,j,k라고 할 때
우리는 n == i+j+k를 만족하는 i,j,k를 찾아야 한다.
3개의 숫자중에서 두개를 알면 다른 하나는 n - (i+j) = k 형태로 얻을 수 있다.
그러므로 i,j를 3의 배수로 반복시키면서 n보다 작은 i+j를 찾을 때마다 카운트를 하면 된다. 
*/
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int i=0,j=0,c=0;

        for(i=3;i<=n;i+=3){
            for(j=3;j<=n;j+=3){
                if(n>i+j) c++;
            }
        }

        System.out.println(c);
    }
}