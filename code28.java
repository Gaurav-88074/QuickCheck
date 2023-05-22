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
public class code28 {
    private int[] arr = {3,2,7,7,1,2};
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
        root.value = Math.min(root.left.value ,root.right.value); 
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
    node discard(node root,int index){
        if(root.low==index && root.high==index){
            // root.value =value;
            return null;
        }
        else if(index<=(root.low+root.high)/2){
            root.left = discard(root.left, index);
        }
        else{
            root.right=discard(root.right, index);
        }
        root.value = Math.min(
            root.left ==null ?Integer.MAX_VALUE :root.left.value ,
            root.right==null ?Integer.MAX_VALUE :root.right.value
        );
        return root; 
    }
    int minRange(node root,int low,int high){
        if(high < root.low || root.high < low){
            return Integer.MAX_VALUE;
        }
        if(low <= root.low && root.high <= high){
            return root.value;
        }
        int left = minRange(root.left, low, high);
        int right = minRange(root.right, low, high);
        return Math.min(left,right);
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
        curr.value = Math.min(curr.left.value ,curr.right.value); 
        return curr;
    }
    public static void main(String[] args) {
        code28 code  = new code28();
        node segmentTree = null;
        segmentTree = code.build(segmentTree, 0, code.arr.length-1);
        // code.inOrder(segmentTree);
        // code.levelOrder(segmentTree);
        // code.update(segmentTree, 3, 10);
        segmentTree = code.discard(segmentTree, 0);
        code.levelOrder(segmentTree);
        System.out.println(code.minRange(segmentTree, 0, 3));
    }
}
// leet code 307