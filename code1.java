
public class code1{
    public void generate(int n,String b,int open,int close,int i){
        if(i==n){
            System.out.println(b);
            return;
        }
        if(open<n){
            generate(n, b+"(", open+1, close,i+1);
        }
        if(open>close){
            generate(n, b+")", open, close+1,i+1);
        }
    } 
    public static void main(String[] args) {
        code1 obj = new code1();
        obj.generate(4, "", 0, 0,0);
    }
}