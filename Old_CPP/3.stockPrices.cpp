#include <iostream>
#include <limits>
#include <vector>
#include <string>
using namespace std;

int highestProfit(vector<int>&stockPrices){
  int current_highest = numeric_limits<int>::min();
  int purchase = stockPrices[0];
  for (size_t i = 1; i < stockPrices.size(); ++i){
    if (stockPrices[i] > purchase){
      purchase = stockPrices[i];
    }
    if (stockPrices[i] < purchase){
      int profit = purchase - stockPrices[i];
      if (profit > current_highest){
        current_highest = profit;
      }
    }
  }
  return current_highest;
}
// To execute C++, please define "int main()"
int main() {
  vector<int>stocks{ 8, 0, 20, 22, 19 };
  cout << highestProfit(stocks) << "\n";
  stocks.push_back(12);
  cout << highestProfit(stocks);
  return 0;
}
