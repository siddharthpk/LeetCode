package Java;

import java.util.*;


//Definition for a binary tree node.
public class TreeNode {
      int val;
      TreeNode left;
      TreeNode right;
      TreeNode() {}
      TreeNode(int val) { this.val = val; }
      TreeNode(int val, TreeNode left, TreeNode right) {
          this.val = val;
          this.left = left;
          this.right = right;
      }
}


class binaryTreePostOrder {
    public List<Integer> preorderTraversal(TreeNode root) {
        // Create a list to store data
        List<Integer> list = new ArrayList<>();

        // Check if root is null
        if(root == null) {
            return list;
        }

        // Add current node val to list
        list.add(root.val);

        // Recursive approach for left subtree

        list.addAll(preorderTraversal(root.left));

        // Recursive approach for right subtree

        list.addAll(preorderTraversal(root.right));

        return list;

    }
}