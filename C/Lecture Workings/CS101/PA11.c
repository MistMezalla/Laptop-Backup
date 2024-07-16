#include <stdio.h>
#include <string.h>

void reverseString(char *str, int start, int end) 
{
    if (start < end) 
    {
        char temp = str[start];
        str[start] = str[end];
        str[end] = temp;

        reverseString(str, start + 1, end - 1);
    }
}

void main() 
{
    char inputString[100];

    printf("Enter a string: ");
    
    fgets(inputString, sizeof(inputString), stdin);
    /*
    for (int i = 0; i < sizeof(inputString); i++) 
    {
        if (inputString[i] == '\n') 
        {
            inputString[i] = '\0';
            break;
        }
    }
    */
   printf("%s\n",inputString);
   printf("%c\n",inputString[6]);
    //gets(inputString);
    int length = strlen(inputString);
    //printf("%d\n",length);
    reverseString(inputString, 0, length-1);

    printf("Reversed string: %s\n", inputString);
}
