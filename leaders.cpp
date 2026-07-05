#include<iostream>
#include<vector>
using namespace std;

int leaders(vector<int> &arr){
    vector<int> result;
    for(int i=0;i<arr.size();i++){
        bool flag = true;
        for(int j=i+1;j<arr.size();j++){
            if(arr[i]<arr[j]){
                flag=false;
                break;
            }
        }
        if(flag){
            result.push_back(arr[i]);
        }
    }
    for(int i=0;i<result.size();i++){
        cout<<result[i]<<" ";
    }
}

int main(){
    vector<int> arr = {10,22,12,3,0,6};
    leaders(arr);
}