#include <iostream>
#include <ctime>
using namespace std;

void DrawBoard(char *space)
{
    cout << "     |     |     " << endl;
    cout << "  " << space[0] << "  |  " << space[1] << "  |  " << space[2] << "   " << endl;
    cout << "_____|_____|_____" << endl;
    cout << "     |     |     " << endl;
    cout << "  " << space[3] << "  |  " << space[4] << "  |  " << space[5] << "   " << endl;
    cout << "_____|_____|_____" << endl;
    cout << "     |     |     " << endl;
    cout << "  " << space[6] << "  |  " << space[7] << "  |  " << space[8] << "   " << endl;
    cout << "     |     |     " << endl;
}

void PlayerMove(char *space, char player){
    int n;
    do{
        cout<<"Enter a spot to mark (1-9): ";
        cin>>n;
        n--;
        if(space[n] == ' '){
            space[n] = player;
            break;
        }
    }while(!n>0 || !n<8);
}

void ComputerMove(char *space, char computer){
    int n;
    srand(time(NULL));
    while(true){
        n = rand() % 9;
        if(space[n] == ' '){
            space[n] = computer;
            break;
        }
    }
}

bool CheckWinner(char *space, char player, char computer){

    if((space[0] != ' ') && (space[0] == space[1]) && (space[1] == space[2])){
        space[0] == player ? cout<<"YOU WIN!"<<endl : cout<<"YOU LOSE"<<endl;
    }
    else if((space[3] != ' ') && (space[3] == space[4]) && (space[4] == space[5])){
        space[3] == player ? cout<<"YOU WIN!"<<endl : cout<<"YOU LOSE"<<endl;
    }
    else if((space[6] != ' ') && (space[6] == space[7]) && (space[7] == space[8])){
        space[6] == player ? cout<<"YOU WIN!"<<endl : cout<<"YOU LOSE"<<endl;
    }
    else if((space[0] != ' ') && (space[0] == space[3]) && (space[3] == space[6])){
        space[0] == player ? cout<<"YOU WIN!"<<endl : cout<<"YOU LOSE"<<endl;
    }
    else if((space[1] != ' ') && (space[1] == space[4]) && (space[4] == space[7])){
        space[1] == player ? cout<<"YOU WIN!"<<endl : cout<<"YOU LOSE"<<endl;
    }
    else if((space[2] != ' ') && (space[2] == space[5]) && (space[5] == space[8])){
        space[2] == player ? cout<<"YOU WIN!"<<endl : cout<<"YOU LOSE"<<endl;
    }
    else if((space[0] != ' ') && (space[0] == space[4]) && (space[4] == space[8])){
        space[0] == player ? cout<<"YOU WIN!"<<endl : cout<<"YOU LOSE"<<endl;
    }
    else if((space[2] != ' ') && (space[2] == space[4]) && (space[4] == space[6])){
        space[6] == player ? cout<<"YOU WIN!"<<endl : cout<<"YOU LOSE"<<endl;
    }
    else{
        return false;
    }
    return true;
}

bool CheckTie(char *space){
    for(int i = 0; i < 9; i ++){
        if(space[i] == ' '){
            return false;
        }
    }

    cout<<"It's A Tie!"<<endl;
    return true;
}

int main()
{
    char space[9] = {
        ' ',
        ' ',
        ' ',
        ' ',
        ' ',
        ' ',
        ' ',
        ' ',
        ' ',
    };
    char player = 'X';
    char computer = 'O';
    bool play = true;

    DrawBoard(space);

    while(play){
        PlayerMove(space, player);
        DrawBoard(space);
        if(CheckWinner(space, player, computer)){
            play = false;
            break;
        }
        else if(CheckTie(space)){
            play = false;
            break;
        }

        ComputerMove(space, computer);
        DrawBoard(space);
        if(CheckWinner(space, player, computer)){
            play = false;
            break;
        }
        else if(CheckTie(space)){
            play = false;
            break;
        }
    }

    cout<<"Thanks for playing"<<endl;

    return 0;
}