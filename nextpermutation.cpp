#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int nextPermutation(vector<int> &nums){
    int ind = -1;
    for(int i=nums.size()-2;i>=0;i--){
        if(nums[i]<nums[i+1]){
            ind = i;
            break;
        }
    }
    if(ind == -1){
        reverse(nums.begin(),nums.end());
    }
    for(int i=nums.size()-1;i>ind;i--){
        if(nums[i]>nums[ind]){
            swap(nums[i],nums[ind]);
        }
    }
    reverse(nums.begin()+ind+1,nums.end());
}

int main(){
    vector<int> nums = {2,1,3};
    nextPermutation(nums);
    for(int i=0;i<nums.size();i++){
        cout<<nums[i]<<" ";
    }
}