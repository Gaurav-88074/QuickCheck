class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {
    }

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}
public class leetcode {
    public static void main(String[] args) {
        StringBuilder path = new StringBuilder();
    }
}
class Solution {
    
    private StringBuilder pathLeft  = new StringBuilder();
    private int foundStart = 0;
    private int foundDest = 0;
    private StringBuilder pathRight = new StringBuilder();
    
    public boolean isFound(TreeNode root,int value){
        if(root==null)return false;
        if(root.val==value) return true;
        boolean left  = isFound(root.left, value);
        boolean right = isFound(root.right, value);
        return left||right;
    }
    public TreeNode LCA(TreeNode root, int startValue, int destValue){
        if(root==null){
            return null;
        }
        TreeNode left  = LCA(root.left , startValue, destValue);
        TreeNode right = LCA(root.right, startValue, destValue);

        if(left!=null)return left;
        if(right!=null)return right;

        if (isFound(root, startValue) && isFound(root, destValue)) {
            return root;
        }
        return null;
    }
    
    public void RouteFromStart(TreeNode root,int startVal){
        if(root==null)return;

        if(root.val==startVal){
            foundStart  =1;
            return;
        }
        if(foundStart==0) RouteFromStart(root.left,startVal);
        if(foundStart==0) RouteFromStart(root.right,startVal);
        
        if(foundStart==1) pathLeft.append("U"); 
            // pathLeft.deleteCharAt(pathLeft.length()-1);
    }
    public void RouteTowardsDest(TreeNode root,int dest){
        if(root==null)return;

        if(root.val==dest){
            foundDest = 1;
            return;
        }
        
        if(foundDest==0){
            pathRight.append("L");
            RouteTowardsDest(root.left, dest);
            if(foundDest==0){
                pathRight.deleteCharAt(pathRight.length()-1);
            }
        }
        if (foundDest==0) {
            pathRight.append("R");
            RouteTowardsDest(root.right, dest);
            if(foundDest==0){
                pathRight.deleteCharAt(pathRight.length()-1);
            }
        }
    }
    public String getDirections(TreeNode root, int startValue, int destValue) {
        TreeNode lcaNode = LCA(root, startValue, destValue);
        System.out.println(lcaNode.val);
        RouteFromStart(lcaNode,startValue);
        RouteTowardsDest(lcaNode, destValue);
        System.out.println(pathLeft);
        return new String();
    }
}