#include<stdio.h>
void main()
{
    char st[]="Hello World!";
    printf("%s\n",st); //Using %c to print entire string reutns garbage value in the form of special symbol(!!), provided no other code 
                       //line is followed after and if so then output is blank.
    int i=0;
    st[0]='J';
    for (i=0;i<13;i++){
        printf("%s ",st[i]); //no output when %s is used to print single char. Even the subsequent lines are not executed.
    }
    printf("Bye\n");

    char string[]="Good Morning!";
    printf("%s\n",string);

    char str[]={'H','i','!','\0'};//try to remove the \0, and check for the changes so occurring.
    
    printf("%s\n",str);

    printf("Out");
}
