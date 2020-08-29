#include <iostream>
#include <limits>
#include <vector>
using namespace std;
  size_t SMALL = 2;
  size_t MEDIUM = 1;
  size_t LARGE = 0;

int highestProduct(vector<int>& numbers){
  vector<int>highestThree(3, std::numeric_limits<int>::min());
  for (size_t i = 0; i < numbers.size(); ++i){
    if (numbers[i] > highestThree[LARGE]){
      highestThree[SMALL] = highestThree[MEDIUM];
      highestThree[MEDIUM] = highestThree[LARGE];
      highestThree[LARGE] = numbers[i];
    }
    else if (numbers[i] > highestThree[MEDIUM]){
      highestThree[SMALL] = highestThree[MEDIUM];
      highestThree[MEDIUM] = numbers[i];
    }
    else if (numbers[i] > highestThree[SMALL]){
      highestThree[SMALL] = numbers[i];
    }
  }
  return highestThree[SMALL] * highestThree[MEDIUM] * highestThree[LARGE];
  
}

// To execute C++, please define "int main()"
int main() {
  auto words = { "Hello, ", "World!", "\n" };
  for (const string& word : words) {
    cout << word;
  }
  vector<int> numbers { 0, 7, 2, -1, 2, 9 };
  cout << highestProduct(numbers);
  return 0;
}
