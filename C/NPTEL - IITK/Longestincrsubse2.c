#include<stdio.h>
void main()
{
    int p,c,l,ml;
    l=0;ml=0;
    scanf("%d",&p);

    while(p!=-1){
        scanf("%d",&c);
        if (p<c){
            l+=1;
        }else if(p==c){
            l+=0;
            if (ml<l){
                ml=l;
                l=1;
            }
        }else{
            l=1;
             if (ml<l){
                ml=l;
                l=1;
            }
        }
        p=c;
    }
printf("%d",ml);
}