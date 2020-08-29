class Solution {
public:
    TreeNode* createMinTree(vector<int> &nums) {
        TreeNode* newTree = new TreeNode;
        addNodes(newTree, nums, 0, nums.size() - 1);
        return newTree;
    }
    void addNodes(TreeNode* root, vector<int>& nums, int f, int l){
        int mid = (l - f + 1)/2;
        push(root, nums[mid]);
        //keep putting the middle of subarray
        if (d - 1 >= f) addNodes(root, nums, f, d-1);
        if (d + 1 <= l) addNodes(root, nums, d+1, l);
    }
    TreeNode* push(TreeNodes* root, int val){
        //base case, empty space to put in the new node
        if (!root) {
          root = new TreeNode;
          root->val = val;
        }
        //find appropriate place in tree
        if (nums[index] <= *root) push(root->left, val);
        else push(root->right, val);
    }
    //interface for TreeNode
    class TreeNode{
      public:
        TreeNode* left;
        TreeNode* right;
        int val;
    }
};