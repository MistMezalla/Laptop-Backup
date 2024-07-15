#include <bits/stdc++.h>
using namespace std;

void pairs()
{
    pair <int, string> p;
    p.first=10;
    p.second="abcd";
    cout << p.first << ' ' << p.second << endl;

    pair <int ,int> p_arr[3];
    int i;
    for (i=0;i<3;i++)
    {
        p_arr[i].first = i*(10-i);
        p_arr[i].second = (i-1)*(7+i);
    }
    
    p_arr[0].first += 3;

    for (i=0;i<3;i++)
    {
        cout << p_arr[i].first << ' '  << p_arr[i].second <<endl;
    }

    pair <int ,string> P ={20,"abcdef"};
    cout << P.first << ' ' << P.second <<endl;
}

void vectors()
{
    vector<int> v(10,3); // if 2nd argument was not giv then def value = 0
    int i;
    for (i=0;i<v.size();i++)
    {
        cout << v[i] <<' ';
    }
    v.push_back(7);
    cout << endl;
    for (i=0;i<v.size();i++)
    {
        cout << v[i] <<' ';
    }

}

void iterators()
{
    vector<pair<int,int>>v = {{1,2},{10,20}};
    vector<pair<int,int>> :: iterator it;

    for (it=v.begin();it < v.end();it++)
    {
        cout << (*it).first << ' ' << (*it).second ;
    }

    cout << endl;
    for (it=v.begin();it < v.end();it++)
    {
        cout << it->first << ' ' << it->second << endl ;
    }

    // for range loops
    for (pair<int,int> &value : v)
        cout << value.first << ' ' << value.second << endl;

    for (auto &value : v)
        value.first+=5;

    for (auto &value : v)
        cout << value.first << ' ' << value.second << endl;

    
}

void maps()
{
    map<pair<string,string>,vector<float>> m;
    m[{"Harshal","Sanas"}].push_back(9.1);
    m[{"Junaid","Islam"}].push_back(8.67);

    for (auto &value: m)
    {
        cout << value.first.first << " " <<value.first.second << "\t:\t" ;
        cout << value.second[0] << endl;
    }

    multimap<pair<string,string>,vector<float>> mm;
    mm.insert({{"Harshal", "Sanas"}, {9.1}});
    mm.insert({{"Junaid", "Islam"}, {8.67}});
    mm.insert({{"Junaid", "Islam"}, {8.8}});


     for (auto &value: mm)
    {
        cout << value.first.first << " " <<value.first.second << "\t:\t" ;
        cout << value.second[0] << endl;
    }
}

int main()
{
    //pairs();
    //vectors();
    //iterators(); 
    maps();

    return 0;
}