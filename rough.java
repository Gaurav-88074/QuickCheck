import java.io.*;
import java.util.*;
class node{
    public int num;
    public int count;
    public node(int a,int b){
        this.num=a;
        this.count=b;
    }
    public String toString(){
        return ""+this.num+" "+this.count;
    }
}
class SortByThis implements Comparator<Object>{

    @Override
    public int compare(Object o1, Object o2) {
        // TODO Auto-generated method stub
        return 0;
    }  
}

public class rough {
    static int mod = 1000000007; 
    public static void main(String[] args) {
        System.out.println();
        TreeSet<Integer> set = new TreeSet<>();
        
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        
        
        Stack<Integer> stack = new Stack<>();
        Queue<Integer> q = new ArrayDeque<>();
    
        StringBuilder res = new StringBuilder();
        
        
        TreeMap<Integer,Integer> map = new TreeMap<>();
        
        Map.Entry<String,Integer> v;
        
        StringBuilder sb = new StringBuilder();
        
        // map.ceilingEntry(6).getKey()
        
        
        
        

        // Map.Entry<Integer, Integer> entry = map.ceilingEntry(6);
        
        // map.getOrDefault(key, defaultValue)
        // map.floorKey(key)
        
        // entry.getKey();
        // entry.getValue();
        // map.getOrDefault(key, defaultValue)
        // map.ceilingKey(key)
        // map.floorEntry(key)
        

    }
}
