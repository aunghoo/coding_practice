//recursive solution
//runtime O(n) where n = number of tree nodes
//memory O(h) where h = heght of the tree (h = log n)
class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        if (!root) return true;
        return symHelper(root, root);
    }

    bool symHelper(TreeNode* left, TreeNode* right){
        if ( (left && !right) || (right && !left) ) return false;
        if ( !left && !right ) return true;
        if (left->val != right->val) return false;
        return symHelper(left->left, right->right) && symHelper(left->right, right->left);
    }
};
