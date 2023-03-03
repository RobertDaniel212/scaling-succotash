#include<iostream>
#include<cmath>
#include<string>
#include<random>
#include<stdlib.h>
using namespace std;

int main(){
//choices

    string opinion;
    string x = "yes";
    string y = "no";
    int sides;
    int rolls;
    //title

    cout << "✯ ✯ ✯ ✯ DICE GAME ✯ ✯ ✯ ✯\n";

    //game end or start

    cout << "DO YOU WANNA PLAY A DICE GAME\n";
    cin >> opinion,"\n";
    if (opinion == x){
        
        cout << "✯ ✯ LETS BEGIN ✯ ✯\n";
        
    } 
    else if (opinion == y){
        
         cout << "✯ ✯ GOODBYE ✯ ✯";
         exit(1);
    }

    //dice roll random library finish later

    random_device rd;   
    mt19937 gen(rd());  
    

    cout << "HOW MANY SIDES DO YOU WANT YOUR DICE TO HAVE(6,12,34): \n";
    cin >> sides;
    cout << "HOW MANY ROLLS DO YOU WANT TO HAVE:";
    cin >> rolls;

    if (sides == 6){
        random_device rd;   
        mt19937 gen(rd());
        uniform_int_distribution<> dist(1,6);
        for (int i = 0; i < rolls; ++i) {
        cout << "YOU ROLLED: " << dist(gen) << " "; 
    }
    }
    if (sides == 12){
        random_device rd;   // non-deterministic generator
        mt19937 gen(rd());
        uniform_int_distribution<> dist(1,12);
        for (int i = 0; i< rolls; ++i){
        cout << "YOU ROLLED: " << dist(gen) << " ";
        }
    }
    if (sides == 34){
        random_device rd;   // non-deterministic generator
        mt19937 gen(rd());
        uniform_int_distribution<> dist(1,34);
        for (int i = 0; i< rolls; ++i){
        cout << "YOU ROLLED: " << dist(gen) << " ";
        }
    }
    return 0;
    
}