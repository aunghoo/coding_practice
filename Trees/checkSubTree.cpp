class Solution {
public:
    //function that checks if the subtree exists inside the root tree
    bool checkSubTree(TreeNode* root, TreeNode* subtree) {
        //base case
        if (!root) return false;
        //check if the current root has same subtree as desired
        if (checkHelper(root, subtree)) return true;
        //check for existence of subtree in either left or right
        return checkSubTree(root->left, subtree) || checkSubTree(root->right, subtree);
    }
    //helper function that finds if root is same as subtree
    bool checkHelper(TreeNode* root, TreeNode* subtree){
        //base cases
        if (!root && !subtree) return true;
        else if ((!root && subtree) || (root && !subtree)) return false;
        if (root->val != subtree) return false;
        //check both left and the right subtrees
        return checkHelper(root->left, subtree->left) && checkHelper(root->right, subtree->right);
    }
    //interface for TreeNode
    class TreeNode{
      public:
        TreeNode* left;
        TreeNode* right;
        int val;
    }
};