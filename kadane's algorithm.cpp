#include<iostream>
#include<vector>
using namespace std;

int maxSubarray(vector<int> &nums){
    int max_num = INT16_MIN;
    for(int i=0;i<nums.size();i++){
        for(int j=i;j<nums.size();j++){
            int sum=0;
            for(int k=i;k<=j;k++){
                sum+=nums[k];
            }
            max_num = max(sum,max_num);
        }
    }
    return max_num;
}

int main()
{
    vector<int> nums= {-2,-3,4,-1,-2,1,5,-3};
    cout<<maxSubarray(nums);
}