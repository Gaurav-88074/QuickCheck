import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class code6 {
    private HashMap<Integer,Integer> map   = new HashMap<>();
    private List<Integer> array= new ArrayList<>();
    private Set<Integer> set= new HashSet<>();

    public int getId(List<Integer> array){
        HashMap<Integer,Integer> m   = new HashMap<>();
        Integer value;
        // map.
        for(int i : array){
            value = m.put(i,1);
            if(value!=null){
                m.put(i, value+1);
            }
        }
        return m.hashCode() + array.get(0) + 
        array.get(1)+
        array.get(2)+
        array.get(3);
    }
    public void compute(int pos,int[] nums,int target,int size){
        // System.out.println("its being called");
        if(size==4 && target==0){
            // if (set.contains(getId(array))) {
            //     return;
            // }
            // set.add(getId(array));
            System.out.println(array.toString());
            return;
        }
        if(pos==nums.length || size==4){
            return;
        }
        int value;
        for (int i = pos; i < nums.length; i++) {
            value = map.get(nums[i]);
            if (value==0) {
                continue;
            }
            map.put(nums[i], value-1);
            
            array.add(nums[i]);
            compute(i+1,nums,target-nums[i],size+1);
            array.remove(array.size()-1);
            map.put(nums[i], value);
        }
        
    }
    public static void main(String[] args) {
        code6 code = new code6();
        int[] nums = {1,0,-1,0,-2,2};
        Integer value;
        for(int i : nums){
            value = code.map.put(i,1);
            if(value!=null){
                code.map.put(i, value+1);
            }
        }
        
        // System.out.println(code.map.toString());
        // Arrays.sort(nums);
        int target = 0;
        code.compute(0,nums,target,0);
        

    }
}
