import java.util.LinkedList;
import java.util.Queue;

class node{
    public int value;
    public int sum;
    public node left;
    public node right;
    public int low;
    public int high;
    //----------------
    public node(int value){
        this.value = value;
        this.left  = null;
        this.right = null;
    }
    //----------------
    public node(){
        this.value = 0;
        this.left  = null;
        this.right = null;
    }
    //----------------

}
public class code8 {
    private int[] arr = {0,9,5,7,3};
    void levelOrder(node root){
        Queue<node> q = new LinkedList<>();
        q.add(root);
        q.add(null);
        while(q.size()!=0){
            node head = q.poll();
            if(head!=null){
                System.out.print(head.value+"("+head.low+"-"+head.high+")"+"  ");
                if (head.left!=null) {
                    q.add(head.left);
                }
                if (head.right!=null) {
                    q.add(head.right);
                }
            }
            else{
                if (q.isEmpty()) {
                    break;
                }
                q.add(head);
                System.out.println();
            }
        }
        System.out.println();
    }
    void inOrder(node root){
        if(root==null){
            return;
        }
        inOrder(root.left);
        System.out.print(root.value+ " ");
        inOrder(root.right);
    }
    void update(node root,int index,int value){
        if(root.low==index && root.high==index){
            root.value =value;
            return;
        }
        else if(index<=(root.low+root.high)/2){
            update(root.left, index, value);
        }
        else{
            update(root.right, index, value);
        }
        root.value = root.left.value + root.right.value;
    }
    int get(node root,int index){
        if(root.low==index && root.high==index){
            return root.value;
        }
        else if(index<=(root.low+root.high)/2){
            return get(root.left, index);
        }
        else{
            return get(root.right, index);
        }
        
    }
    int sumRange(node root,int low,int high){
        if(high < root.low || root.high < low){
            return 0;
        }
        if(low <= root.low && root.high <= high){
            return root.value;
        }
        int left = sumRange(root.left, low, high);
        int right = sumRange(root.right, low, high);
        return left+right;
    }
    node build(node root,int low,int high){
        if(low==high){
            node res = new node(this.arr[low]);
            res.low  = low;
            res.high = high;
            return res; 
        }
        int mid    = (low+high)/2;
        node curr  = new node();
        curr.left  = build(curr.left, low, mid);
        curr.right = build(curr.right, mid+1, high);
        curr.low   = low;
        curr.high  = high;
        curr.value = curr.left.value + curr.right.value; 
        return curr;
    }
    public static void main(String[] args) {
        code8 code  = new code8();
        node segmentTree = null;
        segmentTree = code.build(segmentTree, 0, code.arr.length-1);
        // code.inOrder(segmentTree);
        // code.levelOrder(segmentTree);
        // code.update(segmentTree, 3, 10);
        code.levelOrder(segmentTree);
        System.out.println(code.sumRange(segmentTree, 1, 3));
    }
}
// leet code 307