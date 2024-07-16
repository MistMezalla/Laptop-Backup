#include<stdio.h>
void main()
{
    int l1[]={10,20,30,40};
    printf("%p\n%p\n",&l1,&l1[0]);

    int i;
    for(i=0;i<=4;i++){
        printf("%p ",&l1[i]);
        printf("bytes\n");
    }

    printf("%d\n",*l1);
    int j=0;
    while (j<4){
        printf("%d ",*(l1+j));
        ++j;
    }

    int k=0;
    for(k=0;k<4;++k){
        int n;
        scanf("%d",&n);
        printf("%d\t",n);
        *(l1+k)=n;
        printf("%d '&'",*(l1+k));
    }
    
    int l=0;
    while(l<4){
        printf("%d",l1[l]);
        l++;
    }
}
