#include <iostream>
#include <limits>
#include <vector>
#include <string>
using namespace std;


//does not work for repeated characters
void stringPerms(vector<string>&perms, string str, string prefix){
  if (str.length() == 0){
    perms.push_back(prefix);
  }
  for (size_t i = 0; i < str.length(); ++i){
    string substr = str.substr(0, i) + str.substr(i + 1);
    stringPerms(perms, substr, prefix + str[i]);
  }
}

// To execute C++, please define "int main()"
int main() {
  vector<string>perms;
  string str = "genius";
  stringPerms(perms, str, "");
  for (size_t i = 0; i < perms.size(); ++i){
    cout << perms[i] << "\n";
  }
  return 0;
}
