public class code24 {
    public static boolean checkBit(int value,int index){
        int mask = 1<<index;
        return (value&mask)>0;
    }
    public static  boolean checkBitOne(int value,int index){
        int mask = 1<<index;
        return (value&mask)==0;
    } 
    public static int countLastSet(int value){
        int res = 0;
        int index = 7;
        while(index>-1){
            if(checkBit(value,index)){
                res+=1;
                index-=1;
            }
            else{
                return res;
            }
        }
        return res;
    }
    public static void main(String[] args) {
        // System.out.println(checkBit(3, 0));
        // System.out.println(countLastSet(197));
        // System.err.println(checkBitOne(4, 2));
        
    }
}