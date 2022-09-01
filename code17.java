import java.util.*;
class Kid implements Comparable<Kid>{
    private String name;
    private int age;
    public Kid(String name,int age){
        this.name = name;
        this.age  = age;
    }
    public String toString(){
        return String.valueOf(this.name) +" : "+ String.valueOf(age);
    }
    @Override
    public int compareTo(Kid that) {
        if(this.age!=that.age) return this.age - that.age;
        return this.name.compareTo(that.name);
    }
    // @Override
    // public int hashCode() {
    //     final int prime = 31;
    //     int result = 1;
    //     result = prime * result + ((name == null) ? 0 : name.hashCode());
    //     return result;
    // }
    // @Override
    // public boolean equals(Object obj) {
    //     if (this == obj)
    //         return true;
    //     if (obj == null)
    //         return false;
    //     if (getClass() != obj.getClass())
    //         return false;
    //     Kid other = (Kid) obj;
    //     if (name == null) {
    //         if (other.name != null)
    //             return false;
    //     } else if (!name.equals(other.name))
    //         return false;
    //     return true;
    // }
}
public class code17 {
    public static void main(String[] args) {
        TreeSet<Kid> set = new TreeSet<>();
        set.add(new Kid("ultron", 20));
        set.add(new Kid("Gaurav" ,19));
        set.add(new Kid("Tony"   ,19));
        set.add(new Kid("Vision" ,20));
        System.out.println(set);
        set.remove(new Kid("Gaurav", 19));
        System.out.println(set);
    }
}