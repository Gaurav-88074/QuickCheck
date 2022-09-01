import java.util.*;
class pair{
    
    int a;
    int b;
    
    public pair(int a, int b) {
        this.a = a;
        this.b = b;
    }
    

    @Override
    public int hashCode() {
        final int prime = 31;
        int result = 1;
        result = prime * result + a;
        result = prime * result + b;
        return result;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj)
            return true;
        if (obj == null)
            return false;
        if (getClass() != obj.getClass())
            return false;
        pair other = (pair) obj;
        if (a != other.a)
            return false;
        if (b != other.b)
            return false;
        return true;
    }





    @Override
    public String toString() {
        return "[a=" + a + ", b=" + b + "]";
    }

    
    
}
public class code18 {
    public static void main(String[] args) {
        Set<pair> set = new LinkedHashSet<>();
        set.add(new pair(1, 2));
        set.add(new pair(1, 2));
    
        System.out.println(set);
    }
}
