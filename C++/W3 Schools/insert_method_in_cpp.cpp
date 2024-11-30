#include <bits/stdc++.h>
using namespace std;

int main()
{
    string str = "Hello !!!";
    string to_str = " Wonderful world!!";
    str.insert(5,to_str,0,15); // last index is excluded sim to range in python 
    cout << str << endl;       // Hence o/p: Hello Wonderful worl !!! -> right
                               // and o/p: Hello Wonderful world !!! -> wrong

    return 0;
}