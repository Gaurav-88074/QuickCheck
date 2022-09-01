import java.util.*;
class Cake implements Comparable<Cake>{
    @Override
    public boolean equals(Object obj) {
        // TODO Auto-generated method stub
        return this.price==((Cake)obj).price;
    }
    int price;
    int pound;
    @Override
    public String toString() {
        return "[pound=" + pound + ", price=" + price + "]";
    }
    public Cake(int price, int pound) {
        this.price = price;
        this.pound = pound;
    }
    @Override
    public int compareTo(Cake o) {
        return this.pound - o.pound;
    }
}
public class code19 {
    public static void main(String[] args) {
        Queue<Cake> pq = new PriorityQueue<>();
        pq.add(new Cake(100, 4));
        pq.add(new Cake(200, 3));
        pq.add(new Cake(300, 2));
        pq.remove(new Cake(300, 0));
        System.out.println(pq);
    }
}
