#include<stdio.h>
void main()
{
    int p,c,l,ml;
    l=1;ml=1;
    
    scanf("%d",&p);
    do{
        scanf("%d",&c);
        if (c>p){
            l+=1;
        }else if (c==p){
            l+=0;
            if (ml<l){
                ml=l;
                l=1;
            }
            }else{
                if (ml<l){
                ml=l;
                }
                l=1;
            }
            p=c;
        }while(p!=-1);
        if (ml<l){
                ml=l;
                }
        
        printf("%d",ml);
}

             
            
        
    
