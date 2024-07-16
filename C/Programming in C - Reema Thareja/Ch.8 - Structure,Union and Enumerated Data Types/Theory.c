#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>

//Q1
void Q1()
{
    struct student
    {
        char name[20];
        int roll_no;
    }stud1;

    //For stud1
    gets(stud1.name);
    scanf(" %d",&stud1.roll_no);

    printf("%s\t%d",stud1.name,stud1.roll_no);
}

void Q2()
{
    struct numbers
    {
        int a,b,c;
        int max;
    }num={1,3,2};

    if (num.a>=num.b)
    {
        if (num.a>=num.c)
            num.max=num.a;
        else 
            num.max=num.c;
    }
    else 
        num.max=num.b;
    
    printf("%d",num.max);
}

void Q3()
{
    typedef struct comp_num
    {
        int real,imag;
    }complex;
    
    complex num1={1,2};
    complex num2={3,2};

    printf("%d+j%d",num1.real+num2.real,num1.imag+num2.imag);
}

void Q4()
{
    typedef struct points
    {
        int x,y;
    }pt;

    pt pt1={3,4};
    pt pt2={-5,9};

    float dist=sqrt(pow((pt1.x-pt2.x),2)+pow((pt1.y-pt2.y),2));
    
    printf("%f",dist);
}

void Q6()
{
    typedef struct 
    {
        char name[20];
        int rollno;
    }student;

    student studata[3];

    strcpy(studata[0].name,"Abc");
    studata[0].rollno=12;
    strcpy(studata[1].name,"jnkvb");
    studata[1].rollno=56;
    strcpy(studata[2].name,"Gbhjh");
    studata[2].rollno=79;

    int i;
    for (i=0;i<3;i++)
    {
        printf("%s\t%d\n",studata[i].name,studata[i].rollno);
    }
}

//Q8
typedef struct
    {
        int m,km;
    }dist;

dist add(dist d1,dist d2)
{
    dist d3;
    d3.km=d1.km+d2.km;
    d3.m=d1.m+d2.m;
   
    if (d3.m>=1000)
    {
        d3.km++;
        d3.m-=1000;
    }
    return d3;
}

void Q8()
{

    dist d1,d2;
    printf("Enter the first distance: ");
    scanf(" %d %d",&d1.km,&d1.m);
   
    printf("Enter the second distance: ");
    scanf(" %d %d",&d2.km,&d2.m);
   
    printf("%d and %d",add(d1,d2).km,add(d1,d2).m);
}

//Q9
typedef struct
{
    int h,m,s;
}time;

time t1,t2;

time sub(time t1,time t2)
{
    time t3;
    if (t1.h>=t2.h)
    {
        t3.h=t1.h-t2.h;
        t3.m=t1.m-t2.m;
        t3.s=t1.s-t2.s;
    }
    else
    {
        t3.h=t2.h-t1.h;
        t3.m=t2.m-t1.m;
        t3.s=t2.s-t1.s;  
    }
   
    if (t3.s<0)
    {
        t3.m--;
        t3.s+=60;
    }
    if (t3.m<0)
    {
        t3.h--;
        t3.m+=60;
    }

    return t3;
}

void Q9()
{
    time t1,t2;
    printf("Enter the first time: ");
    scanf(" %d %d %d",&t1.h,&t1.m,&t1.s);
   
     printf("Enter the second time: ");
    scanf(" %d %d %d",&t2.h,&t2.m,&t2.s);
   
    printf("%d %d %d",sub(t1,t2).h,sub(t1,t2).m,sub(t1,t2).s);
}

typedef struct
{
    int rollno;
    char name[20];
}student;

void Q10()
{
    student *pstu,stud1;
    pstu=&stud1;
    pstu->rollno=20;
    gets(pstu->name);
   
    printf("%s\t%d",pstu->name,pstu->rollno);
}

void Q12()
{
    student *pstu[2];

    int i;
    for (i=0;i<2;i++)
    {
        pstu[i]=(student *)malloc(1*sizeof(student));
        
        printf("Enter the detalis of the student%d: \n",i+1);
        //fgets(pstu[i]->name, sizeof(pstu[i]->name), stdin);
        //gets(pstu[i]->name);
        scanf("%s",pstu[i]->name);
        scanf("%d",&pstu[i]->rollno);
        //gets(pstu[i]->name);
    }
        
    for (i=0;i<2;i++)
    {
        printf("The detalis of the student%d: \n",i+1);
        printf("%s\t%d\n",pstu[i]->name,pstu[i]->rollno);
    }
}

//Q14
typedef struct
{
    int m;
    int cm;
}height;

height* add_height(height *h1,height *h2)
{
    height *h3,h3_np;
    h3=&h3_np;

    h3->cm=h1->cm+h2->cm;
    h3->m=h1->m+h2->m;

    if (h3->cm>=60)
    {
        h3->cm-=60;
        h3->m++;
    }
    return h3;
}
void Q14()
{   
    height h1_np,h2_np;
    height *h1,*h2;
    h1=&h1_np;
    h2=&h2_np;
    h1->m=1;
    h1->cm=67;
    h2->m=1;
    h2->cm=83;   
    printf("%d %d",add_height(h1,h2)->m,add_height(h1,h2)->cm);
    //printf("Hi");
}

//union0
void unoin_working()
{
    union stu
    {
        int roll;
        char name[20];
    }student;

    scanf(" %s",student.name);
    printf("%d %s",student.roll,student.name);

    student.roll=20;
    printf("%d %s\n",student.roll,student.name);
}
/*
As expected when overwritting the data of diff data type say int overwritting on string then
garbage data is overwritten in the string variable.
*/

void main()
{
    Q14();
}
