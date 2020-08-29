class Solution {
public:
    std::unordered_map<int, int> combinations;
    int numTrees(int n) {
        //base cases
        if (n == 0) return 0;
        if (n == 1) return 1;
        if (n == 2) return 2;
        //memoization
        if (combinations.find(n)!=combinations.end()) return combinations[n];
        //recursion
        int both_sides = 0;
        for (int i = 1; i < n - 1; ++i){
            both_sides += (numTrees(i) * numTrees(n - i - 1));
        }
        combinations[n] = (2 * numTrees(n - 1)) + both_sides;
        return combinations[n];
    }
};