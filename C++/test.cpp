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

void test1()
{
    vector<int> v ={1,2,3,1,5,4,2,3,6,7,4,2};
    
    int i;
    for (i=0;i<v.size();i++)
        cout << v[i];
    
    cout << endl;
    /*
    set<int>s = set(v);
    for (i=0;i<v.size();i++)
        cout << v[i];
    */

    set<int> s(v.begin(), v.end());
    for (int elem : s)
        cout << elem << " ";
    cout << endl;
}

int main()
{
//overflow();
/*
string str="Team";
cout << str << endl << str[4];
return 0;
*/
/*
string command = "G()(al)";
int i;
int j=1;
for (i=j;i<command.length();i++)
{
    cout << command[i];
}
*/
test1();
}
