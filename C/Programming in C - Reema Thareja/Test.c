#include <stdio.h>
#include <math.h>
int test1()
{
   int a,b;
   b=4;
   printf("\n %d\t",10 + ++b); 
   printf("%d\t",ceil((int)1.5));

   int nd=5;
   a=floor((float)nd/2);
   printf("%d",a);

   int x=2,y=3,z=4;
   if (z!=100)
      x=10;
   else
      y=10;
   if (x+y>10)
      z=12;
      x=20;
      y=z++;
   printf("\t%d\t%d\t%d\t",x,y,z);
   x=y==z;
   printf("%d\t",x);
   printf("%d\t",y>10||y&&z<0||x>0);

   int m,n=2;
   //printf("%d\t%d",m,m+n);
   printf("\n%d",'F');
   //n=!n;
   printf("\t%d",-n);
   m=n++;
   printf("\t%d\t%d",m,n);
   m++;
   ++n;
   printf("\t%d\t%d",m,n);
   printf("\t%d",m+++n);
   printf("\t%d",m);
   x=10;
   printf("\n%d",x);
   if(x=y<z)
   if(y)
      z=10;
   else
   {
      printf("hi");
      z=20;
   }
   printf("\n%d\t%d\t%d\n",x,y,z);

   switch('A')
   {
      default :
         printf("Def\t");
      case 'a':
      //while (0)
      
      case 'A':
         printf("HELLO\t");
         break;
      
      case 'b':
      case 'B':
         printf("BYe\t");
         break;
      
   }  
   printf("\n");
   int w=15;
   if (x<y)
   if(x>z)
      printf("HI\n");
   else if(z<w)
      printf("BYe\n");
   if (x==w)
      printf("Hello\n");
   else
      printf("Get lost\n");
   
   int num=10;
   for (;num<=10;num++)
      printf("%d\t",num);

   int i=0;
   n=10;
   while(i==0)
   {
      if (n<10)
      //printf("Phew");
      break;
      n--;
      printf("Haa");
   }
   printf("\n%d\n",n);

   //printf("%d\t",k>10);

   
   /*
   int j=1;
   while(j<=10)
      {
      j=1;
      printf("%d",j);
      j++;
      }
   */
  //printf("%d",~-3);

   int p,q;
   for (p=1,q=1;p<3||q<=5;p++,q++)
      printf("%d\t%d\n",p,q);
 int l[9]={0};
 }

void update(int **n,int *m)
{
    *n=m;
}

void *Update(int *n,int *m)
{
    n=m;
}

void test2()
{
   int a=10;
   int *ptr1,*ptr2;
   ptr2=&a; 
   //update(&ptr1,ptr2);
   //printf("%d ",*ptr1);
   Update(ptr1,ptr2);
   printf("%d ",*ptr1);
}

#include <stdio.h>

void test3() {
    int a = 10;
    int *p = &a;

    // Ensure proper sequencing of operations
    int temp1 = ++*p;  // Increment the value pointed to by p (i.e., a)
    int temp2 = *p++;  // Read the value pointed to by p and then increment p
    int temp3 = *p++;  // Read the next value pointed to by the incremented p

    // Print the values
    printf("%d\t%d\t%d\t%d", a, temp1, temp2, temp3);
}

struct node {
int value;
struct node *next;
};
void rearrange(struct node *list) {
struct node *p, *q;
int temp;
if (!list || !list -> next) return;
p = list; q = list -> next;
while(q) {
temp = p -> value; p->value = q -> value;
q->value = temp; p = q ->next;
q = p ? p ->next : 0;
}
}


void test4() {
   struct node *list=NULL;
   struct node *p1,*p2,*p3,*p4,*p5,*p6,*p7;
   list=p1;
   p1->value=1; p1->next=p2;
   p2->value=2; p2->next=p3;
   p3->value=3;p3->next=p4;
   p4->value=4;p4->next=p5;
   p5->value=5;p5->next=p6;
   p6->value=6;p6->next=p7;
   p7->value=7;p7->next=NULL;
   rearrange(list);

   printf("%d %d %d %d %d %d %d",p1->value,p2->value,p3->value,p4->value,p5->value,p6->value,p7->value);
}

void main()
{
   printf(" %d",'4'-'7');
}

