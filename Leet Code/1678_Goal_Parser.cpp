#include <bits/stdc++.h>
using namespace std;

class Solution 
{
    public:
        string interpret(string command) 
        {
            string buff,ret_str;
            int i;
            for (i=0;i<command.length();i++)
            {
                buff.push_back(command[i]);
                switch(buff)
                {
                    case 'G':
                        ret_str.push_back('G');
                        
                }
            }

        }
};