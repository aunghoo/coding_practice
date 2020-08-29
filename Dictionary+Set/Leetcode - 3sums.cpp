class Solution {
public:
    struct pair_hash {
        inline std::size_t operator()(const std::pair<int,int> & v) const {
            return v.first*31+v.second;
        }
    };
    //this does in O(n^2) time and O(1) memory
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector< vector<int> >triplets;
        std::sort(nums.begin(), nums.end());
        std::unordered_set< std::pair<int,int>, pair_hash >seen;
        for (int first = 0; first < (int)nums.size() - 2; ++first){
            int second = first + 1;
            int third = (int)nums.size() - 1;//last element
            while (second != third){
                if (-nums[third] < nums[first] + nums[second] ) {
                    --third;          
                }
                else if (-nums[third] > nums[first] + nums[second]) {
                    ++second;
                }
                else {
                    vector<int>trip{ nums[first], nums[second], nums[third] };
                    sort(trip.begin(), trip.end());
                    std::pair<int, int>part(trip[0], trip[1]);
                    if (seen.find(part) == seen.end()){
                        seen.insert(part);
                        triplets.push_back(trip);
                    }                    
                    ++second;
                }
            }
        }
        return triplets;
    }
};