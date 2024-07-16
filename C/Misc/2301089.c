#include <stdio.h>

char *sum(char *);
void main()
{
        char str[200];
        printf("Enter the string: ");
        gets(str);

        printf("Entered string: %s",str);

        char c='a';
        char C='A';
        int ind=0;
	  int flag=0;
	  while (1)
        {
                if (str[ind]==c || str[ind]==C)
                {
                        flag=1;
                        c++;
                        C++;
                }
                else if(c=='z' || C=='Z')
                        break;
                else
                        break;
        }

        if (flag==1)
                printf("\nEntered string contains all alphabets in English");
        else
                printf("\nEntered string does not contains all alphabets in English");

	 printf("\n");
        int sum=0;
        char str_new[200];

        int j=0,k=0;
        while(str[j] != '\0')
        {
                if (str[j] != ' ')
                {
                        if (str[j]>='0' && str[j]<='9')
                        {
                                switch(str[j])
                                {
                                        case '0':
                                                sum+=0;
                                                break;
                                        case '1':
                                                sum+=1;
                                                break;
                                        case '2':
                                                sum+=2;
                                                break;
                                        case '3':
                                                sum+=3;
                                                break;
                                        case '4':
                                                sum+=4;
                                                break;
                                        case '5':
                                                sum+=5;
                                                break;
                                        case '6':
                                                sum+=6;
                                                break;
                                        case '7':
                                                sum+=7;
                                                break;
                                        case '8':
                                                sum+=8;
                                                break;
                                        case '9':
                                                sum+=9;
                                                break;
                                }
                        }

                        str_new[k]=str[j];
                        j++;
                        k++;
                }
		else
		 {
                        str_new[k]='=';
                        k++;
                        str_new[k]=sum;
                        k++;
                        str_new[k]=' ';
                        k++;
                        j++;
                        sum=0;
                }
        }
        str_new[k]='\0';

        printf("\nSum of digits: %s",str_new);

}

char *sum(char *word)
{
        int sum=0,cnt=0;
        static char str_new[200];

        int i=0;
        while(*word+i != '\0')
        {
                if (*word+i != ' ' || *word+i !='\0')
                {
                        if (*word+i>='0' && *word+i<='9')
                                sum+=(int)(*word+i);
                        str_new[i]=*word+i;
                        i++;
                }
                else
                {
                        str_new[i]='=';
                        i++;
                        str_new[i]=(char)(sum);
                        i++;
                        str_new[i]=' ';
                        i++;
                }
        }
        str_new[i]='\0';

        return str_new;
}

              