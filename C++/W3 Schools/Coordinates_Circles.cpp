#include <bits/stdc++.h>
using namespace std;

class Coordinates
{
    public:
        int x,y;
    
        void print()
        {
            cout <<"The coordinates are: ("<< x << ',' << y <<')' << endl ;
        }

        void set_x(int abs)
        {
            x = abs;
        }

        void set_y(int ord)
        {
            y = ord;
        }

        float dist_bet_pts(Coordinates p1, Coordinates p2)
        {
           return sqrt(pow((p1.x - p2.x),2) + pow((p1.y - p2.y),2));
        }
};

int main()
{
    Coordinates P1,P2;
    P1.set_x(3);
    P1.set_y(4);
    P1.print();

    P2.set_x(-7);
    P2.set_y(10);
    P2.print();

    cout << endl;
    auto originalFlags = cout.flags();
    cout << fixed << setprecision(2);
    cout << P1.dist_bet_pts(P1,P2) << endl;

    cout.flags(originalFlags);
    cout << 15.23154 << endl;
    return 0;
}