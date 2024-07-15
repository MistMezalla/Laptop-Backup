#include <bits/stdc++.h>
using namespace std;

void overflow()
{
int a = 100000;
int b = 100000;
long int c = a * b;
long int d = a * 1L * b;
cout << c << endl << d << "\n";
cout << INT_MAX;
}

void strings()
{
string str="Team";
cout << str << endl;

int i;
string str_rev;

for (i=str.length()-1;i>-1;i--)
{
    str_rev.push_back(str[i]);
}
/*
for (i=0;i<str.length();i++)
{
    str_rev.push_back(str[i]);
}
*/
cout <<  str_rev;

}

int main()
{
//overflow();
strings();


return 0;
}
