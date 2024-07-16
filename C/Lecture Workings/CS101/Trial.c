#include <stdio.h>
#include <string.h>
int main()
{
    char str[100];
    printf("Enter the string that you want to reverse wordwise :");
   // fgets(str, 100, stdin);
    gets(str);//better to use here bcz strlen will not count '\n' then
    printf("The reverse wordwise string :");
   
    for (int i = strlen(str); i >= 0; i--) // for running the looop in reverse
    {
        
        if (str[i] == ' ' || i == 0) // when we get blank space or get the first character then forward printing
        {
            if (i == 0) // if we get the first character
            {
                i = -1; // for running the loop from j=0
            }
            for (int j = i + 1; str[j] != '\0' && str[j] != ' '; j++)//we are quiting the loop when and condiotin fails
            {
                printf("%c", str[j]); //for printing string
            }
            printf(" ");//for printing spacaes btw words
        }
        
    }
    return 0;
}
