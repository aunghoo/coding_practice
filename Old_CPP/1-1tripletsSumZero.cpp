//faster algorithm, makes use of unordered set which has O(1) lookup time
void fasttriplets(vector<int>&all, vector< vector<int> >&triplets){
    std::unordered_map<int, int> map;
    for (int i = 0; i < all.size(); ++i){
        int key = all[i];
        map[key] = 1;
    }
    for (int i = 0; i < all.size() - 1; ++i){
        for (int j = i + 1; j < all.size(); ++j){
            int last = (-1) * (all[i] + all[j]);
            if (map.find(last) != map.end()){
                //if found
                triplets.push_back(vector<int>{ all[i], all[j], last});
            }
        }
    }
}

//[ 5 0 3 2 -5 1 -6 ]
//sorted [ -6 -5 0 1 2 3 5 ]
//[ -6 -3 -1 0 3 5 9 10 11 ]
//sort first then find the triplets in O(n^2) time and O(1) memory
void fastertriplets(vector<int>&all, vector< vector<int> >&triplets){
    std::sort(all.begin(), all.end());
    for (int first = 0; first < (int)all.size() - 2; ++first){
      int second = first + 1;
      int third = (int)all.size() - 1;//last element
      while (second != third){
        if (-all[third] < all[first] + all[second] ) {
          --third;          
        }
        else if (-all[third] > all[first] + all[second]) {
          ++second;
        }
        else {
          triplets.push_back(vector<int>{ all[first], all[second], all[third] });
          ++second;
        }
      }
    }
}




int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    vector<int> vec{5, 0, 3, 2, -5, 1, -6};
    vector< vector<int> >trips;
    fasttriplets(vec, trips);
    for (int i = 0; i < trips.size(); ++i){
        for (int j = 0; j < 3; ++j){
            cout << trips[i][j] << " " ;
        }
        cout << "\n";
    }
    return 0;
}
