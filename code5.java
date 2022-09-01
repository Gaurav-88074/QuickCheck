public class code5 {
    public static boolean strongPasswordCheckerII(String password) {
        boolean isDigit = false;
        boolean lc = false;
        boolean uc = false;
        boolean sc = false;
        String schr = "!@#$%^&*()-+";
        boolean together  =true;
        if(password.length()<8){
            return false;
        }
        char pre = '.';
        for(char c : password.toCharArray()){
            
            if( (c) <= 57 && (c) >= 48 ){
                isDigit = true;
                System.out.println("cleared for digit");
            }
            if(c<=122 && c >=97 ){
                System.out.println("cleared for lower");
                lc = true;
            }
            if(c<=90 && c>=65){
                System.out.println("cleared for upper");
                uc = true;
            }
            if(schr.contains(String.valueOf(c) )){
                System.out.println("cleared for sepecial");
                sc = true;
            }
            if(c==pre){
                System.out.println("cleared for adj");
                together = false;
                
            }
            pre = c;
        }
        return isDigit && lc && uc && sc && together;
    }
    public static void main(String[] args) {
        strongPasswordCheckerII("j1A!A!A!");
    }
}
