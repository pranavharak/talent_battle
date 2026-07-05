#include<iostream>
#include<vector>
using namespace std;
int maxProfit(vector<int>& prices) {
    // int buy,sell,index;
    // int m = INT_MAX;
    // for(int i=0;i<prices.size();i++){
    //     if(prices[i]<m){
    //         m = prices[i];
    //         buy = prices[i];
    //         index=i;
    //     }
    // }
    // int mi=INT_MIN;
    // for(int i=index;i<prices.size();i++){
    //     if(prices[i]>mi){
    //         mi = prices[i];
    //         sell = prices[i];
    //     }
    // }
    // return abs(buy-sell);
    int mini = prices[0];
    int max_profit = 0;
    for(int i=0;i<prices.size();i++){
        int cost = prices[i] - mini;
        max_profit = max(max_profit,cost);
        mini = min(mini,prices[i]);
    }
    return max_profit;
}

int main(){
    vector<int> prices = {7,1,5,3,6,4};
    cout<<maxProfit(prices);
}