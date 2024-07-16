#include <stdio.h>
#include <ctype.h>
#include <string.h>
void main()
{
    char str[1000];
    printf("Enter the string: ");
    gets(str);
    puts(str);

    //int i,ind,j,c=0;
    int l=strlen(str);
    printf("%d\n",l);

    char word[100];
    gets(word);
    puts(word);

    int i;
    int freq=0;
    for(i=0;i<=l;i++)
    {
        if (isblank(str[i])==0 && ispunct(str[i])==0)
            printf("%c",str[i]);
        else
            printf("\n");
    }    
    /*
    for (i=0;i<=l;i++)
    {
        printf("\thi\t");
        if (isblank(str[i])==0 && ispunct(str[i])==0)
        {
        //if (str[i]!=' ' && str[i]!='\0')
            c++;
            printf("%c",str[i]);
            printf("%d\n",c);
        }
        else
        {
            ind=i;
            printf("%d",i);
        }
    */
        /*
        for (j=ind-c;j<ind;j++)
            printf("%c",str[j]);
        
        //c=0;
    }
    */
}
