import java.io.*;
import java.util.*;

public class rough {
    public static void main(String[] args) {
        System.out.println();
        TreeSet<Integer> set = new TreeSet<>();
        
        TreeMap<Integer,Integer> map = new TreeMap<>();
        Map.Entry<Integer, Integer> entry = map.ceilingEntry(6);
        
        // map.getOrDefault(key, defaultValue)
        // map.floorKey(key)
        
        entry.getKey();
        entry.getValue();
        // map.getOrDefault(key, defaultValue)
        // map.ceilingKey(key)
        // map.floorEntry(key)

    }
}
