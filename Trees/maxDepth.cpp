//Top-down approach
//TIme complexity: O(n) where n = number of tree nodes
//Memory complexity: O(d) where d = maximum depth of the tree, d = log n if BST
class Solution {
public:
    //top-down approach
    int current_max;
    int maxDepthTopDown(TreeNode* root) {
        current_max = 0;
        maxHelper(root, 0);
        return current_max;
    }
    void maxHelper(TreeNode* node, int depth_sofar){
        if (!node){
            current_max = std::max(current_max, depth_sofar);
            return;
        }
        maxHelper(node->left, depth_sofar + 1);
        maxHelper(node->right, depth_sofar + 1);
    }
};


//Bottom-up approach
//TIme complexity: O(n) where n = number of tree nodes
//Memory complexity: O(d) where d = maximum depth of the tree, d = log n if BST
class Solution {
public:
    //bottom-up approach
    int current_max;
    int maxDepthBotUp(TreeNode* root) {
        if (!root) return 0;
        return std::max(maxDepthBotUp(root->left), maxDepthBotUp(root->right)) + 1;
    }
};
