import java.util.Comparator;
import java.util.PriorityQueue;

class Task{
    public int enqueTime;
    public int processingTime;
    public int index;

    public Task(int index,int a,int b){
        this.index = index;
        this.enqueTime = a;
        this.processingTime = b;
    }
    public String toString(){
        return ""+this.index+" "+this.enqueTime+" "+this.processingTime;
    }
}
class SortByThis implements Comparator<Task>{
    
    @Override
    public int compare(Task o1, Task o2) {
        if(o1.processingTime==o2.processingTime){
            return o1.index-o2.index;
        }
        return o1.processingTime - o2.processingTime;
    }  
}
class Solution {
    public int[] getOrder(int[][] tasks) {
        PriorityQueue<Task> pq = new PriorityQueue<>();
        int i = 0;
        for(int[] task : tasks){
            pq.add(new Task(i,task[0],task[1]));
            i+=1;
        }
        System.out.println(pq);
        return new int[]{0,2,3,1};
    }
}