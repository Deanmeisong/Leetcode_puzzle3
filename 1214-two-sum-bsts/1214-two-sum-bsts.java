/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private List<Integer> nums1 = new ArrayList<>();
    private List<Integer> nums2 = new ArrayList<>();

    private void inorder(TreeNode root, List<Integer> nums) {
        if (root == null) {
            return;
        }
        inorder(root.left, nums);
        nums.add(root.val);
        inorder(root.right, nums);
    }

    public boolean twoSumBSTs(TreeNode root1, TreeNode root2, int target) {
        inorder(root1, nums1);
        inorder(root2, nums2);
        int i = 0;
        int j = nums2.size() - 1;
        while (i < nums1.size() && j >= 0) {
            int sum = nums1.get(i) + nums2.get(j);
            if (sum == target) {
                return true;
            }
            if (sum < target) {
                i++;
            } else {
                j--;
            }
        }
        return false;
    }
}