#include<iostream>
#include<vector>
using namespace std;
int sorArray(vector<int> &nums){
    int low=0,mid=0,high=nums.size() - 1;
    while(mid<=high){
        if(nums[mid]==0){
            swap(nums[low],nums[mid]);
            low++;
            mid++;
        }
        else if(nums[mid]==1){
            mid++;
        }
        else{
            swap(nums[mid],nums[high]);
            high--;
        }
    }
}
int main(){
    vector<int> nums = {0,0,1,2,1,0,2,1,2};
    cout<<"before= ";
    for(int i =0;i<nums.size()-1;i++){
        cout<<nums[i];
    }
    sorArray(nums);
    cout<<"after= ";
    for(int i =0;i<nums.size()-1;i++){
        cout<<nums[i];
    }
}