import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String s=("@".repeat(n*3)+"\n").repeat(n), s3=("@".repeat(n) + " ".repeat(n*3) + "@".repeat(n) + "\n").repeat(n), s2=("@".repeat(n) + " ".repeat(n*2) + "@".repeat(n) + "\n").repeat(n);
        System.out.print(s3+s2+s+s2+s3);
    }
}