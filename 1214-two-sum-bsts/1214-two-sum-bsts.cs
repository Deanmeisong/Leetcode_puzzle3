/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    private List<int>[] nums = new List<int>[2] { new List<int>(), new List<int>() };

    private void Inorder(TreeNode root, int i)
    {
        if (root == null) return;
        Inorder(root.left, i);
        nums[i].Add(root.val);
        Inorder(root.right, i);
    }

    public bool TwoSumBSTs(TreeNode root1, TreeNode root2, int target) {
        Inorder(root1, 0);
        Inorder(root2, 1);
        int i = 0, j = nums[1].Count - 1;

        while (i < nums[0].Count && j >= 0)
        {
            int sum = nums[0][i] + nums[1][j];
            if (sum == target) return true;
            if (sum < target) i++;
            else j--;
        }

        return false;
    }
}