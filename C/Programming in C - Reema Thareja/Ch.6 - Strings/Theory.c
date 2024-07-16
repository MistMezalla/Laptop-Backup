#include <stdio.h>

//printf() with strings
void printf_str()
{
    char str[]="Good Morning to Everyone";
    int len;
    len=sizeof(str)/sizeof(str[0])-1;
    printf("%d\n",len);
    printf("|%20.20s|\n",str);
    printf("|%20.30s|\n",str);
    printf("|%26.30s|\n",str);
    printf("|%-26.30s|\n",str);
    printf("|%20.0s|\n",str);
    printf("|%25.30s|\n",&str[3]);
}

//sprintf() with strings
void sprintf_str()
{
    char str[1000]="Good Morning to Everyone";
    sprintf(str,"%s","Good Bye to all");
    printf("%s\n",str);
}

//sprintf usage
void sprintf_use()
{
    char buffer[100]; // buffer to store the formatted string
    int num = 10;
    float fnum = 3.14;

    // Format a string with integer and float values
    sprintf(buffer, "Integer: %d, Float: %.2f", num, fnum);

    // Print the formatted string
    printf("Formatted string: %s\n", buffer);
    printf("\n");
    //printf("%c \n",buffer[0]);
    int i;
    for (i=0;i<10 && buffer[i] != '\0';i++)
    {
        printf("%c ",buffer[i]);
    }
}
/*
The sprintf() will store each and every literal printed as a 'string' into a buffer location
*/

//sscanf
void sscanf_str() {
    char str[1000] = "10 20.15 HaHaHa";
    int intValue;
    float floatValue;
    char string[100];

    // Use pointers to variables in sscanf
    sscanf(str, "%d %f %s", &intValue, &floatValue, string);

    printf("%s",str);
}

//sscanf usage
void sscanf_use()
{
    char str[] = "John25 35";
    char name[20];
    int age;

    // Extracting data from the string
    sscanf(str, "%s %d", name, &age);

    // Outputting the extracted data
    printf("Name: %s\n", name);
    printf("Age: %d\n", age);
}
//Q8
void Q8()
{
    char str1[]="Hello Bye";
    char str2[]="Hello bye";

    int l1,l2;
    l1=sizeof(str1)/sizeof(str1[0])-1;
    l2=sizeof(str2)/sizeof(str2[0])-1;

    int i,flag;
    if (l1<=l2)
    {
        for (i=0;i<l1;i++)
        {
            if(str1[i]<str2[i])
            {
                printf("Str1 < Str2");
                printf("*\n");
                flag=0;
                break;
            }

            else if(str1[i]>str2[i])
            {
                printf("Str1 > Str2");
                flag=0;
                break;
            }
            else
                flag=1;
        }
        if (flag==1)
        {
            printf("Equal");
            printf("#\n");
        }    
    }   

    else if (l1>=l2)
    {
        for (i=0;i<l2;i++)
        {
            if(str1[i]<str2[i])
            {
                printf("Str1 < Str2");
                printf("***\n");
                flag=0;
                break;
            }

            else if(str1[i]>str2[i])
            {
                printf("Str1 > Str2");
                flag=0;
                break;
            }
            else 
                flag=1;
        }
        if (flag==1)
        {
            printf("Equal");
            printf("###\n");
        }
    }   
}

//Q11
void Q11()
{
    char str1[]="Hello Everyone";
    int l1;
    l1=sizeof(str1)/sizeof(str1[0])-1;

    int l;
    printf("Enter the number of right char to be extracted: ");
    scanf(" %d",&l);

    char str2[l+1];
    int i,j=l1;
    for (i=l;i>-1;i--)
    {
        str2[i]=str1[j];
        j--;
    }

    printf("%s",str2);
}

//Q12
void Q12()
{
    char str1[]="Hello Everyone";
    int l1;
    l1=sizeof(str1)/sizeof(str1[0])-1;

    int i;
    int pos,l;
    printf("Enter the postion and the length of the string: ");
    scanf(" %d %d",&pos,&l);

    char str2[l];
    int j=0;
    for(i=pos;i<pos+l;i++)
    {
        printf("*\n");
        str2[j]=str1[i];
        j++;
    }
    str2[j]='\0';

    printf("%s",str2);
}

//Q13
//Wrong and diff output everywhere.
void Q13()
{
    char str1[]="Hello present here.";
    int l1;
    l1=sizeof(str1)/sizeof(str1[0])-1;

    int i;
    char str2[]="to everyone";
    int l2,pos=6;
    l2=sizeof(str2)/sizeof(str2[0])-1;

    l1+=l2;
    
    for (i=l1;i>=(pos-1)+l2;i--)
    {
        str1[i]=str1[i-l2];
    }
    
    int j=0;
    for (i=pos-1;i<pos-1+l2;i++)
    {
        str1[i]=str2[j];
        j++;
        //printf("%c",str1[i]);
    }

    //printf("%s",str1);
}

void test1()
{
    char str[]="hello bye";
    int l=sizeof(str)/sizeof(str[0])-1;
    printf("\n%c",str[l-1]);
    
    ++l;
    str[l]=str[l-1];
    str[l-1]='H';
    printf("\n%s",str);
    printf("\n%c",str[l-2]);
}

//Q15
void Q15()
{
    char str1[]="How dou you?";
    int l1=sizeof(str1)/sizeof(str1[0])-1;
    
    char str2[]="are";
    int l2=sizeof(str2)/sizeof(str2[0])-1;
    int i,j;

    char str3[]="dou";
    int l3=sizeof(str3)/sizeof(str3[0])-1;


    int flag;
    for (i=0;i<l1;i++)
    {
        if (str1[i]==str3[0])
        {
            printf("%d\n",i);
            for (j=1;j<l2;j++)
            {
                if (str1[i+j]==str3[j])
                {
                    flag=1;
                    printf("f1 = %d \n",j);
                }
                else
                {
                    printf("%c,%c\n",str1[i+j],str3[j]);
                    flag=0;
                    printf("f0 = %d \n",j);
                    break;
                }
            }
        }
        if (flag==1)
        {
            printf("Entered\n");
            for(j=0;j<l2;j++)
            {
                str1[i+j]=str2[j];
            }
            break;
        }
    }

    printf("%s",str1);
}

#include <string.h>
//String Func
void str_func()
{
    char str1[]="Hello to Everyone";
    char str2[]="Good Morning to all";
    char str3[]="to";

    int ch;
    do
    {
        printf("\nEnter the choice: ");
        scanf(" %d",&ch);

        switch(ch)
        {
            case 1: //strcat
            {
                strcat(str1,str2);
                printf("%s",str1);
                break;
            }
            case 2: //strncat
            {
                strncat(str1,str2,5);
                printf("%s",str1);
                break;
            }
            case 3: //strcmp
            {
                printf("%d",strcmp(str1,str2));
                break;
            }
            case 4: //strncmp
            {
                printf("%d",strncmp(str1,str2,10));
                break;
            }
            case 5://strchr
            {
                printf("%c",*strchr(str1,'o'));
                break;
            }
            case 6: //strrchr
            {
                printf("%d",*strrchr(str1,'o'));
                break;
            }
            case 7: //strcpy
            {
                strcpy(str1,str2);
                printf("%s",str1);
                break;
            }
            case 8: //strncpy
            {
                strncpy(str1,str2,5);
                printf("%s",str1);
                break;
            }
            case 9: //strstr
            {
                printf("%c",*strstr(str1,str3));
                break;
            }
            case 10: //strspn
            {
                printf("%d",strspn(str1,str2));
                break;
            }
            case 11: //strcspn
            {
                printf("%d",strcspn(str1,str2));
                break;
            }
            case 12: //strpbrk
            {
                printf("%c",*strpbrk(str1,str2));
                break;
            }
        }
    }while(ch!=0);
}

//Q17
void Q17()
{
    char stu_nm[5][10]={"Rahul","Rohan","Mohan","Shardul","krishna"};

    int i,j;
    //printf("%s",stu_nm[1]);

    for (i=0;i<5;i++)
    {
        for (j=i+1;j<5;j++)
        {
            if(strcmp(stu_nm[i],stu_nm[j])>=0)
            {
                char temp[10];
                strcpy(temp,stu_nm[i]);
                strcpy(stu_nm[i],stu_nm[j]);
                strcpy(stu_nm[j],temp);
            }
        }
    }

    for(i=0;i<5;i++)
        printf("%s\n",stu_nm[i]);
}

//Q18
void Q18()
{
    char str[10];
    char ch;
    printf("enter the string until '*': ");
    ch=getchar();

    int i=0;
    while(i<10 && ch!='*')
    {
        str[i]=ch;

        ch=getchar();
        i++;
    }
    str[i]='\0';
    printf("The string is \n%s",str);
}

#include <ctype.h>
//Q19
void Q19()
{
    char str[50];
    fgets(str,sizeof(str),stdin);
    int word=0;
    int l=0;
    /*
    l=sizeof(str)/sizeof(str[0]);
    printf("%d",l);
    */
    int i;
    for (i=0;i<50;i++)
    {
        if (str[i]=='\0')
            break;
        else
            l++;
    }
    printf("%d\n",l);
    printf("%c\n",str[13]);
    for (i=0;i<l;i++)
    {
        if (ispunct(str[i])!=0 || isspace(str[i])!=0)
        {
            printf("%d\n",i);
            word++;
        }    
            
    }
    printf("%d",word-1);
}

//Q20
void Q20()
{
    char para[100];
    char ch;
    ch=getchar();
    int l=0;
    while(ch!='*')
    {
        para[l]=ch;
        l++;
        ch=getchar();
    }
    para[l]='\0';
    printf("%s\n",para);
    //printf("%d\n",l);
    
    int word=0,line=0;
    int i;
        
    for(i=0;i<l;i++)
    {
        if(i!=0)
        {
            //word
            if(ispunct(para[i])!=0 || isspace(para[i])!=0)
                word++;
            //line
            if (para[i]=='.')
                line++;
        }
    }
    printf("char=%d\n",l);
    printf("words= %d\nlines = %d",word,line);

}

//Q22
void Q22()
{
    char str[]="Heloo, My name is Sohan, I am 10 year old. ";
    int l=sizeof(str)/sizeof(str[0])-1;

    int i;
    for (i=0;i<l;i++)
    {
        if(str[i]==',')
            str[i]=';';
    }

    printf("%s",str);

}

//Q23
//Wrong output everywhere.
void Q23()
{
    char para[100];
    fgets(para, sizeof(para), stdin);
    int l=0;
    int i;
    for (i=0;i<100;i++)
    {
        if(para[i]=='\0')
            break;
        l++;
    }    
    l--;//Reducing the count of newline character due to fgets
    printf("%s\n",para);
    printf("%c\n",para[35]);
    printf("%d\n",l);
    
    int line=1;
   
    for(i=0;i<l;i++)
    {
        if(i==0)
        {
            printf("%d.",line);
            while(para[i]!='.')
            {
                printf("%c",para[i]);
                i++;
            }
            printf("%c\n",para[i]);
            line++;
        }
        else if (para[i]=='.')
        {
            printf("%d.",line);
            i++;
            while(para[i]!='.')
            {
                printf("%c",para[i]);
                i++;
            }
            printf("%c\n",para[i]);
            line++;
        }
    }

}

void Q23_TB()
{
    char para[100];
    fgets(para, sizeof(para), stdin);
    int l=strlen(para)-1;
    
    printf("%s\n",para);

    int i=0,line=1;
    while(i<l)
    {
        if (i==0)
        {
            printf("%d.",line);
            line++;
        }
        else if(para[i]=='.' && i!=l-1)
        {
            printf(".\n%d.",line);
            line++;
            i++;
        }
        printf("%c",para[i]);
        i++;
    }
}

void main()
{
    Q23_TB();
    //printf("%d",printf("Hello = %d\t",10)); = 8 of char + 2 of int + 1of \t
    /*
    int i;
    for(i=0;i<10;i++)
    {
        printf("%d",i);
        i++;
        i++;
    }
    */
}
