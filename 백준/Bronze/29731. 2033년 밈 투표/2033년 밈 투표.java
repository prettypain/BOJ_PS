import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
class Main{
    public static boolean is_in(String[] arr, String target){
        for(int i=0; i<arr.length; i++){
            if(arr[i].equals(target)) return true;
        }
        return false;
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = {"Never gonna give you up", "Never gonna let you down", "Never gonna run around and desert you", "Never gonna make you cry", "Never gonna say goodbye", "Never gonna tell a lie and hurt you", "Never gonna stop"};
        String str;
        int n = Integer.parseInt(br.readLine());
        boolean t = true;
        for(int i=0; i<n; i++){
            str = br.readLine();
            if(!Main.is_in(s, str)) t = false;
        }
        System.out.println(t ? "No" : "Yes");
    }
}