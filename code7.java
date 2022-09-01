import java.math.BigInteger;

public class code7 {
    public static void main(String[] args) {
        BigInteger num1 = new BigInteger("10");
        BigInteger num2 = new BigInteger("20");
        BigInteger num3 = num1.add(num2);
        System.out.println(num3.toString(2));
    }
}
