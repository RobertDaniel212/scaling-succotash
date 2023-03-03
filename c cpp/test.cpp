#include <iostream>
#include <cstdlib>
#include <time.h>
using namespace std;

 //main program
int main()
{
 int guess;//user guess for the value of the dice
 float bet;//the bet placed by the user
 float possibility;//number of combinations each number can come
 int dice1, dice2;//the random value between 1-6 for each dice
 int total;//the total number after the value of dice1 and dice2 is added
 float earned_or_lost_money;//earned or lost money depending on whether you win/lose

srand(time(0));//random number seed


cout << endl;//blank line

cout << " What do you guess the result will be?(2-12): ";
cin >> guess;//user input for guess

cout << " Enter amount of money to bet ($1-$1000): ";
cin >> bet;//user input for bet

cout << endl;//blank line

dice1 = rand() % 6 + 1;//value of first dice(1-6)
dice2 = rand() % 6 + 1;//value of second dice(1-6)

total = dice1 + dice2;//value of dice1+dice2

switch (guess)// values for possible combinations for the total value of the dices added
{

case 2: possibility = 1; break;
case 3: possibility = 2; break;
case 4: possibility = 3; break;
case 5: possibility = 4; break;
case 6: possibility = 5; break;
case 7: possibility = 6; break;
case 8: possibility = 5; break;
case 9: possibility = 4; break;
case 10: possibility = 3; break;
case 11: possibility = 2; break;
case 12: possibility = 1; break;
}//switch



cout << " For your $" << bet << " bet, the roll is" << endl;
cout << endl;//blank line

if (dice1 == 1)//drawing if the value of dice1 is 1
{
    cout << "=============" << endl;
    cout << "|           |" << endl;
    cout << "|     1     |" << endl;
    cout << "|           |" << endl;
    cout << "=============" << endl;
}//if
else if (dice1 == 2)//drawing if the value of dice1 is 2
{
    cout << "=============" << endl;
    cout << "| 2         |" << endl;
    cout << "|           |" << endl;
    cout << "|         2 |" << endl;
    cout << "=============" << endl;
}//else if
else if (dice1 == 3)//drawing if the value of dice1 is 3
{
    cout << "=============" << endl;
    cout << "| 3         |" << endl;
    cout << "|     3     |" << endl;
    cout << "|         3 |" << endl;
    cout << "=============" << endl;
}//else if
else if (dice1 == 4)//drawing if the value of dice1 is 4
{
    cout << "=============" << endl;
    cout << "| 4       4 |" << endl;
    cout << "|           |" << endl;
    cout << "| 4       4 |" << endl;
    cout << "=============" << endl;
}//else if
else if (dice1 == 5)//drawing if the value of dice1 is 5
{
    cout << "=============" << endl;
    cout << "| 5       5 |" << endl;
    cout << "|     5     |" << endl;
    cout << "| 5       5 |" << endl;
    cout << "=============" << endl;
}//else if
else if (dice1 == 6)//drawing if the value of dice1 is 6
{
    cout << "=============" << endl;
    cout << "| 6       6 |" << endl;
    cout << "| 6       6 |" << endl;
    cout << "| 6       6 |" << endl;
    cout << "=============" << endl;
}//else if

cout << endl;//blank line 

if (dice2 == 1)//drawing if the value of dice2 is 1
{
    cout << "=============" << endl;
    cout << "|           |" << endl;
    cout << "|     1     |" << endl;
    cout << "|           |" << endl;
    cout << "=============" << endl;
}//if
else if (dice2 == 2)//drawing if the value of dice2 is 2
{
    cout << "=============" << endl;
    cout << "| 2         |" << endl;
    cout << "|           |" << endl;
    cout << "|         2 |" << endl;
    cout << "=============" << endl;
}//else if
else if (dice2 == 3)//drawing if the value of dice2 is 3
{
    cout << "=============" << endl;
    cout << "| 3         |" << endl;
    cout << "|     3     |" << endl;
    cout << "|         3 |" << endl;
    cout << "=============" << endl;
}//else if
else if (dice2 == 4)//drawing if the value of dice2 is 4
{
    cout << "=============" << endl;
    cout << "| 4       4 |" << endl;
    cout << "|           |" << endl;
    cout << "| 4       4 |" << endl;
    cout << "=============" << endl;
}//else if
else if (dice2 == 5)//drawing if the value of dice2 is 5
{
    cout << "=============" << endl;
    cout << "| 5       5 |" << endl;
    cout << "|     5     |" << endl;
    cout << "| 5       5 |" << endl;
    cout << "=============" << endl;
}//else if
else if (dice2 == 6)//drawing if the value of dice2 is 6
{
    cout << "=============" << endl;
    cout << "| 6       6 |" << endl;
    cout << "| 6       6 |" << endl;
    cout << "| 6       6 |" << endl;
    cout << "=============" << endl;
}//else if

cout << endl;//blank line
cout << " For a total of " << total << endl;
cout << endl;//blank line


if (guess == total)//if the user guessed correctly
{

    earned_or_lost_money = bet * 8 / possibility;//calculation for money earned

    cout << " You were correct... since " << guess << " can come up " << possibility << " ways," << endl;
    cout << "You win $" << bet << "*8/" << possibility << "= $" << earned_or_lost_money << endl;
}//if

else//if the user guessed wrong 
{

    earned_or_lost_money = possibility * bet;//calculation for lost money

    
    cout << " You were wrong... since " << guess << " can come up " << possibility << " ways," << endl;
    cout << " You lost " << possibility << "*$" << bet << "= $" << earned_or_lost_money << " dollars!!!!!!" << endl;
    cout << " Thanks for your donation :)" << endl;
}//else
return 0;
}//end