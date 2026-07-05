#include<iostream>
#include<vector>
using namespace std;

void setZeros(vector<vector <int>> &matrix){
    // for(int i=0;i<matrix.size();i++){
    //     for(int j=0;j<matrix[i].size();j++){
    //         if(matrix[i][j]==0){
    //             for(int k=0;k<matrix.size();k++){
    //                 matrix[k][j] = -1;
    //             }
    //             for(int k=0;k<matrix[i].size();k++){
    //                 matrix[i][k] = -1;
    //             }
    //         }
    //     }
    // }
    // for(int i=0;i<matrix.size();i++){
    //     for(int j=0;j<matrix[i].size();j++){
    //         if(matrix[i][j]==-1){
    //             matrix[i][j]=0;
    //         }
    //     }
    // }
}

int main(){
    vector<vector<int>> mat ={{1,1,1},{1,0,1},{1,1,1}};
    for(int i = 0; i < mat.size(); i++){
        for(int j = 0; j < mat[i].size(); j++){
            cout << mat[i][j] << " ";
        }
        cout << endl;
    }
    setZeros(mat);
    for(int i = 0; i < mat.size(); i++){
        for(int j = 0; j < mat[i].size(); j++){
            cout << mat[i][j] << "  ";
        }
        cout << endl;
    }
}