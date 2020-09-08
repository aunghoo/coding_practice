void phoneNumberToString(map <string, vector<string>>& mapping, string digits, vector<string>&possibilities) {
    for (int s = 0; s < (int)mapping[string(1,digits[0])].size(); ++s){
        possibilities.push_back(mapping[string(1, digits[0])][s]);
    }
     for (int i = 1; i < digits.length(); ++i){
         string digit = string(1, digits[i]); // just casting char back to string
         int currentsize = (int)possibilities.size();
         for (int j = 0; j < (int)mapping[digit].size() - 1; ++j){
            //duplicate previous entries by the amount of variations current digit can add
            for (int s = 0; s < currentsize; ++s){
                possibilities.push_back(possibilities[s]);
            }
        }
         int pos = 0; 
         for (auto it : mapping[digit]){
             for (int k = 0; k < currentsize; ++k){
                possibilities[pos] += it;
                ++pos;
             }
         }
     }
}
//////////////// BOTTOM UP
/*
def phone_permute_list(digits, mapping):
      if len(digits) == 0:
        return ['']
      else:
        result = []
        for x in phone_permute_list(digits[1:], mapping):
          for y in mapping[digits[0]]:
            result.append(y + x)
        return result

*/

int main()
{
    map <string, vector<string> > dict;

    dict["1"].push_back("A");
    dict["1"].push_back("B");
    dict["1"].push_back("C");
    
    dict["2"].push_back("D");
    dict["2"].push_back("E");
    dict["2"].push_back("F");
    
    dict["3"].push_back("G");
    dict["3"].push_back("H");
    dict["3"].push_back("I");
    
    dict["4"].push_back("J");
    dict["4"].push_back("K");
    dict["4"].push_back("L");
    
    string digits = "123";
    vector<string>p;
    phoneNumberToString(dict, digits, p);
    for (string i : p) cout << i << "\n";
    
    return 0;
}
