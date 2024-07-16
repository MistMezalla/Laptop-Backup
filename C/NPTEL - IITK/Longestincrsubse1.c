#include<stdio.h>
void main()
{
    int p,c,len;
    len=0;
    int maxlen=0;
    
    scanf("%d",&p);
    if(p!=-1){
        len=1;maxlen=1;
        scanf("%d",&c);
        while(!(c==-1)){
            if (p<c){
                len+=1;
            }else if (p==c){
                len+=0;
                if (maxlen<len){
                    maxlen=len;
                }
            }
            else{
                if (maxlen<len){
                    maxlen=len;
                }
                len=1;
            }
            p=c;
            scanf("%d",&c);
        }
    if (maxlen<len){
        maxlen=len;
    }
    }
    printf("%d",maxlen);

}
