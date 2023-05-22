import java.util.Scanner;
import java.util.*;
public class code27 {
    public static void main(String[] args) {
        Scanner sc  = new Scanner(System.in);
        String s = sc.next();

        char pre = '#';
        int c = 0;
        StringBuilder res = new StringBuilder();
        for(int i =0 ;i <s.length() ; i++);{
            if(pre==s.charAt(i)){
                c+=1;
            }
            else{
                int v = Math.min(2, c);
                c = 1;
            }
            pre = s.charAt(i);
        }

    }
}
