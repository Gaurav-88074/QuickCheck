public class code25 {
    // public final int mod = 1000000000 + 7;
    static int powr( int a , long b ) {
        int mod = 1000000007;
        int res = 1; 
 
        while (b > 0) {
            if ((b & 1) != 0)
                res = res * a;
            res%=mod;
            b = b >> 1; 
            a = a * a; 
            a%=mod;
        }
        return res % mod;
    }
    public static void main(String[] args) {
        System.out.println(powr(4,25));
    }
}
