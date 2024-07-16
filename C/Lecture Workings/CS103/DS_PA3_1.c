#include<stdio.h>
#include<stdlib.h>
#include<math.h>

//Q1
void Q1()
{
    int n;
    printf("Enter the size of the array: ");
    scanf(" %d",&n);

    int *arr=(int *)calloc(n,sizeof(int));

    int i;
    printf("Enter the elements of the array: \n");
    for (i=0;i<n;i++)
        scanf(" %d",&arr[i]);

    for (i=0;i<n;i++)
        printf("%d ",arr[i]);
    printf("\n");

    int min=arr[0],pos=0;
    for (i=1;i<n;i++)
    {
        if (arr[i]<=min)
        {
            min=arr[i];
            pos=i;
        }
    }

    arr[0]=arr[0]+arr[pos];
    arr[pos]=arr[0]-arr[pos];
    arr[0]=arr[0]-arr[pos];

    int j;
    for (i=1;i<n;i++)
    {
        for(j=i-1;j>=0;j--)
        {
            if(arr[i]>=arr[j])
            {
                pos=j+1;
                break;
            }
        }

        int temp;
        temp=arr[i];
        for (j=i;j>=pos+1;j--)
            arr[j]=arr[j-1];
        arr[pos]=temp;
    }

    for (i=0;i<n;i++)
        printf("%d ",arr[i]);
    printf("\n");
}

//Q2
struct student_t 
{
    char *name;
    int roll;
    float cpi;
};

int m = 0, n = 3;
typedef struct student_t* student;
typedef int (*Comparator)(student, student);

int compareRoll(student a, student b) 
{
    return a->roll > b->roll ? 1 : 0;
}

int compareCPI(student a, student b) 
{
    return a->cpi > b->cpi ? 1 : 0;
}

void sortStudents(student *p, int m, Comparator c) 
{
    int i;
    for (i = 1; i < m; i++) 
    {
        student key = p[i];
        int j = i - 1;
        while (j >= 0 && c(p[j], key)) 
        {
            p[j + 1] = p[j];
            j = j - 1;
        }
        p[j + 1] = key;
    }
}

student* createArray(int size)
{
    student* arr = (student*)calloc(size,sizeof(student));
    return arr;
}

student createStudent()
{
    student s;
    s = (student)calloc(1, sizeof(struct student_t));
    s->name = (char*)calloc(500, sizeof(char));
    getchar();
    printf("Enter name of the student\n");
    scanf("%[^\n]s",s->name);
    printf("Enter the roll number of the student\n");
    scanf("%d", &s->roll);

    printf("Enter the cpi of the student\n");
    scanf("%f", &s->cpi);

    return s;
}

int getChoice()
{
    int choice;

    printf("Enter your choice: \n");
    printf("1=Insert an element at the end\n");
    printf("2=Insert an element at the beginning\n");
    printf("3=Insert an element at the ith location\n");
    printf("4=Delete an element from the end\n");
    printf("5=Delete an element from the beginning\n");
    printf("6=Delete an element from the ith location\n");
    printf("7=Sort by roll\n");
    printf("8=Sort by cpi\n");
    printf("9=Display the array\n");
    printf("10=Exit the program\n");

    scanf(" %d",&choice);

    return choice;
}

void display(student *arr)
{
    int i;
    for(i = 0; i < m; i++)
        printf("Name: %s Roll: %d CPI: %f\n",arr[i]->name,arr[i]->roll,arr[i]->cpi);
}

student* insertAtEnd(student *arr)
{
    
    student stud = createStudent();
    
    if (m < n)
    {
        arr[m] = stud;
        m++;
        
        return arr;
    }
    else
    {
        n = ceil(1.2 * (n));

        student* newArr = createArray(n);
        int i;
        for (i = 0; i < m; i++)
            newArr[i] = arr[i];

        newArr[n-1] = stud;
        m++;
        free(arr);
        return newArr;
    }
}

student* insertAtBeginning(student* arr)
{
    student stud = createStudent();
    if(m < n)
    {
        m++;
        
        shiftRight(arr,0);
        arr[0] = stud;
        
        return arr;
    }
    else
    {
        n = ceil(1.2 * (n));

        student* newArr = createArray(n);

        int i;
        for (i = 0; i < m; i++)
            newArr[i+1] = arr[i];

        newArr[0] = stud;
        m++;

        free(arr);
        return newArr;
    }
}

void shiftRight(student* arr, int pos)
{
    int i=m-1;
    while(i>=pos)
    {
        arr[i]=arr[i-1];
        i--;
    }
}

student* insertAtI(student* arr)
{
    int index;
    
    printf("Enter the location you want to insert the element");
    scanf("%d",&index);
    
    student stud = createStudent();
    
    if(index > m-1){
    arr[m-1] = stud;
    return arr;
    }
    else if(index <= 0){
        arr[0] = stud;
        return arr;
    }
    
    m++;
    
    if(m<=n)
    {
        shiftRight(arr,index);
        arr[index] = stud;
        return arr;
    }
    
    n = ceil(1.2 * n);
    student* newArr = createArray(n);
    
    int i;
    for(i = 0; i < m; i++)
    newArr[i] = arr[i];
    
    shiftRight(arr,index);
    
    arr[index] = stud;
    
    free(arr);
    return newArr;
}

student* deleteAtEnd(student* arr)
{
    if(m==0)
    printf("The array is already empty there is nothing to delete");
    
    free(arr[--m]);
    
    
    if(m < 0.5*n)
    {
        n = ceil(0.75*n);
        student* newarr = createArray(n);
        
        int i;
        for(i = 0; i < m; i++)
        newarr[i] = arr[i];
        
        free(arr);
        return newarr;
    }
    else
    return arr;
}

void shiftLeft(student* arr,int index)
{
    int i=0;
    for(i = index; i < m-1;i++)
        arr[i]=arr[i+1];
}

student* deleteAtBeginning(student* arr)
{
    if(m==0)
    printf("The array is already empty there is nothing to delete");
    
    free(arr[0]);
    shiftLeft(arr,0);
    m--;
    
    if(m < 0.5*n)
    {
        n = ceil(0.75*n);
        student* newarr = createArray(n);
        
        int i;
        for(i = 0; i < m; i++)
        newarr[i] = arr[i];
        
        free(arr);
        
        return newarr;
    }
    else
    return arr;
    
}

student* deleteAtI(student* arr)
{
    int index;
    printf("Enter the location of the element you want to delete\n");
    scanf("%d",&index);
    
    if(index<=0)
    return deleteAtBeginning(arr);
    
    if(index>=m)
    return deleteAtEnd(arr);
    
    m--;
    
    free(arr[index]);
    shiftLeft(arr, index);
    
    if(m<0.5*n)
    {
        n = ceil(0.75*n);
        student *newArr = (student*)calloc(n, sizeof(student));
        int i;
        for(i=0;i<m;i++)
            newArr[i]=arr[i];
        free(arr);
        return newArr;
    }
    return arr;
}

void Q2()
{
   student *p = createArray(n);

    int ch;
   do
    {
        ch = getChoice();
        switch(ch)
        {
            case 1:
                p = insertAtEnd(p);
                break;
            case 2:
                p = insertAtBeginning(p);
                break;
            case 3:
                p = insertAtI(p);
                break;
            case 4:
                p = deleteAtEnd(p);
                break;
            case 5:
                p = deleteAtBeginning(p);
                break;
            case 6:
                p = deleteAtI(p);
                break;
            case 7:
                sortStudents(p, m, compareRoll);
                break;
            case 8:
                sortStudents(p, m, compareCPI);
                break;
            case 9:
                display(p);
                break;
            case 10:
                exit(0);
                break;
            default:
                printf("Invalid Input!!\n");
        }
    }while (ch!=10);
}

void main()
{
    Q2();
}