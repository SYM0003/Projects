#include<bits/stdc++.h>
using namespace std;
const int X=1,O=-1,empty=0;
int board[3][3];
int currentplayer;
void clearboard(){
    for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){
            board[i][j]=empty;
        }
        currentplayer=X;
    }
}
void putdata(int cell){
    int i=0,j=0;
    if(cell==1){i=0,j=0;}
    if(cell==2){i=0,j=1;}
    if(cell==3){i=0,j=2;}
    if(cell==4){i=1,j=0;}
    if(cell==5){i=1,j=1;}
    if(cell==6){i=1,j=2;}
    if(cell==7){i=2,j=0;}
    if(cell==8){i=2,j=1;}
    if(cell==9){i=2,j=2;}
    if(board[i][j]==X||board[i][j]==O){
        cout<<"Warning(wrong cell selected!)"<<endl;
        cout<<"Please select empty cell only"<<endl;
    }
    else{
        board[i][j]=currentplayer;
        currentplayer=-currentplayer;
    }
}
bool iswin(int marks){
    int win=3*marks;
    return (board[0][0]+board[0][1]+board[0][2]==win||
           board[1][0]+board[1][1]+board[1][2]==win||
           board[2][0]+board[2][1]+board[2][2]==win||
           board[0][0]+board[0][1]+board[0][2]==win||
           board[1][0]+board[1][1]+board[1][2]==win||
           board[2][0]+board[2][1]+board[2][2]==win||
           board[0][0]+board[1][1]+board[2][2]==win||
           board[0][2]+board[1][1]+board[2][0]==win
           );

}

int getwinner(){
    if(iswin(O)){
        return O;
    }
    else if(iswin(X)){
        return X;
    }
    return empty;
}

void printBoard() {
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            switch (board[i][j]) {
                case X: cout << "X"; break;
                case O: cout << "O"; break;
                case empty: cout << " "; break;
            }
            if (j < 2) cout << "|";
        }
        if (i < 2) cout << "\n-+-+-\n";
    }
    cout<<endl;
}

int main(){
    clearboard();
    printBoard();

    for(int i=0;i<9;i++){
        cout<<"Player call :"<<(currentplayer==1?"X":"O")<<endl;
        cout<<"Enter the cell No(empty cell only)."<<endl;
        int cell;
        cin>>cell;
        putdata(cell);
        printBoard();

    }
    int winner=getwinner();
    if(winner!=0){
        cout<<(winner==X?"X":"O")<<" wins"<<endl;
    }
    else{
        cout<<"Tie"<<endl;
    }
}