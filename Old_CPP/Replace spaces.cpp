#include <iostream>
using namespace std;


void replaceSpaces(string& str, int trueLength){
  //clean extraneous chars
  str.erase(str.begin()+trueLength, str.end());
  //first loop to obtain the last position in the modified string
  int numspaces = 0;
  for (int i=0; i < trueLength; ++i){
     if (str[i] == ' '){
         ++numspaces;
     }
  }
  int index = trueLength + numspaces * 2;
  
  for (int i = trueLength; i < index; ++i){
    str.push_back('a'); 
  }
  //loop through to put in '%02'
  for (int i = trueLength - 1; i >= 0; --i){
    if (str[i] == ' '){
      str[index - 1] = '2';
      str[index - 2] = '0';
      str[index - 3] = '%';
      index -= 3;
    }
    else {
      str[index-1] = str[i]; 
      --index;
    }
  }
  cout << str;
}

// To execute C++, please define "int main()"
int main() {
  string str = "well my friend  ";
  replaceSpaces(str, 14); 
  return 0;
}