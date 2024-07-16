#include <stdio.h>
void main()
{
    int rom_lit[7]={1000,500,100,50,10,5,1};

    int num;
    printf("Enter the number whose roman equivalent is to be found: ");
    scanf(" %d",&num);
    
    int rem;
    rem=num;

    int i=0;
    check:
    while(rem)
    {
        //printf("*%d\t",rem);
            if(rem>=rom_lit[i])
            {
                rem-=rom_lit[i];
                //printf("&%d\t",rem);
                
                switch (rom_lit[i])
                {
                    case 1:
                        printf("I");
                        break;
                    case 5:
                        printf("V");
                        break;
                    case 10:
                        printf("X");
                        break;
                    case 50:
                        printf("L");
                        break;
                    case 100:
                        printf("C");
                        break;
                    case 500:
                        printf("D");
                        break;
                    case 1000:
                        printf("M");
                        break;
                }
                
            
           //printf("%d\n",rem);
        }
        else    
            i++;
    }
}