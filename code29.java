import java.util.*;
class node{
    public int data;
    public node(int data) {
        this.data =data;
    }
    public node sum(int value){
        this.data+=value;
        return this;
    }
    @Override
    public String toString() {
        return String.valueOf(this.data);
    }
}
public class code29{
    public static void main(String[] args) {
        node obj = new node(100);
        System.out.println(obj.sum(10).sum(20));
        List<Integer> l = new ArrayList<>();
        
    }
}