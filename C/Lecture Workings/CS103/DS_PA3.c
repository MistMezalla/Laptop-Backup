#include <stdio.h>
#include <stdlib.h>
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
    for (i=0;i<n;i++)
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
/*
//Q2
struct student_t {
    char *name;
    int roll;
    float cpi;
};

typedef struct student_t *Student;
typedef int (*Comparator)(Student, Student);

int compareRoll(Student a, Student b) {
    return a->roll > b->roll ? 1 : 0;
}

int compareCPI(Student a, Student b) {
    return a->cpi > b->cpi ? 1 : 0;
}

void sortStudents(Student *p, int m, Comparator c) 
{
    for (int i = 1; i < m; i++) {
        Student key = p[i];
        int j = i - 1;
        while (j >= 0 && c(p[j], key)) {
            p[j + 1] = p[j];
            j = j - 1;
        }
        p[j + 1] = key;
    }
}

void printStudent(Student s) {
    printf("Name: %s, Roll: %d, CPI: %.2f\n", s->name, s->roll, s->cpi);
}

void insertElementAtEnd(Student **p, int *m, int *n) 
{
    if (*m < *n) {
        (*p)[*m] = (Student)malloc(sizeof(struct student_t));
        printf("Enter student details:\n");
        printf("Name: ");
        scanf("%ms", &((*p)[*m]->name));
        printf("Roll: ");
        scanf("%d", &((*p)[*m]->roll));
        printf("CPI: ");
        scanf("%f", &((*p)[*m]->cpi));
        (*m)++;
    } else {
        *n = (int)(1.2 * (*n));
        *p = (Student *)realloc(*p, (*n) * sizeof(Student));
        insertElementAtEnd(p, m, n);
    }
}

void insertElementAtBeginning(Student **p, int *m, int *n) 
{
    if (*m < *n) {
        for (int i = *m; i > 0; i--) {
            (*p)[i] = (*p)[i - 1];
        }
        (*p)[0] = (Student)malloc(sizeof(struct student_t));
        printf("Enter student details:\n");
        printf("Name: ");
        scanf("%ms", &((*p)[0]->name));
        printf("Roll: ");
        scanf("%d", &((*p)[0]->roll));
        printf("CPI: ");
        scanf("%f", &((*p)[0]->cpi));
        (*m)++;
    } else {
        *n = (int)(1.2 * (*n));
        *p = (Student *)realloc(*p, (*n) * sizeof(Student));
        insertElementAtBeginning(p, m, n);
    }
}

void insertElementAtLocation(Student **p, int *m, int *n, int location) 
{
    if (location > *m - 1) {
        location = *m - 1;
    }

    if (*m < *n) {
        for (int i = *m; i > location; i--) {
            (*p)[i] = (*p)[i - 1];
        }
        (*p)[location] = (Student)malloc(sizeof(struct student_t));
        printf("Enter student details:\n");
        printf("Name: ");
        scanf("%ms", &((*p)[location]->name));
        printf("Roll: ");
        scanf("%d", &((*p)[location]->roll));
        printf("CPI: ");
        scanf("%f", &((*p)[location]->cpi));
        (*m)++;
    } else {
        *n = (int)(1.2 * (*n));
        *p = (Student *)realloc(*p, (*n) * sizeof(Student));
        insertElementAtLocation(p, m, n, location);
    }
}

void deleteElementFromEnd(Student **p, int *m, int *n) 
{
    if (*m > 0) {
        free((*p)[*m - 1]->name);
        free((*p)[*m - 1]);
        (*m)--;
    }

    if (*m < 0.5 * (*n)) {
        *n = (int)(0.75 * (*n));
        *p = (Student *)realloc(*p, (*n) * sizeof(Student));
        *m = (int)(0.75 * (*n));
    }
}

void deleteElementFromBeginning(Student **p, int *m, int *n) 
{
    if (*m > 0) {
        free((*p)[0]->name);
        free((*p)[0]);

        for (int i = 1; i < *m; i++) {
            (*p)[i - 1] = (*p)[i];
        }

        (*m)--;
    }

    if (*m < 0.5 * (*n)) {
        *n = (int)(0.75 * (*n));
        *p = (Student *)realloc(*p, (*n) * sizeof(Student));
        *m = (int)(0.75 * (*n));
    }
}

void deleteElementFromLocation(Student **p, int *m, int *n, int location) 
{
    if (location < 0) {
        location = 0;
    } else if (location >= *m) {
        location = *m - 1;
    }

    if (*m > 0) {
        free((*p)[location]->name);
        free((*p)[location]);

        for (int i = location + 1; i < *m; i++) {
            (*p)[i - 1] = (*p)[i];
        }

        (*m)--;
    }

    if (*m < 0.5 * (*n)) {
        *n = (int)(0.75 * (*n));
        *p = (Student *)realloc(*p, (*n) * sizeof(Student));
        *m = (int)(0.75 * (*n));
    }
}

void printMenu() {
    printf("\nMenu:\n");
    printf("1. Insert an Element at the End\n");
    printf("2. Insert an Element at the Beginning\n");
    printf("3. Insert an Element at the ith Location\n");
    printf("4. Delete an Element from the End\n");
    printf("5. Delete an Element from the Beginning\n");
    printf("6. Delete an Element from the ith Location\n");
    printf("7. Sort by Roll\n");
    printf("8. Sort by CPI\n");
    printf("9. Print Students\n");
    printf("0. Exit\n");
}

void Q2() {
    int n = 3, m = 0;
    Student *p = (Student *)calloc(n, sizeof(Student));

    int choice;
    do {
        printMenu();
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                insertElementAtEnd(&p, &m, &n);
                break;
            case 2:
                insertElementAtBeginning(&p, &m, &n);
                break;
            case 3:
                printf("Enter the index to insert: ");
                int index;
                scanf("%d", &index);
                insertElementAtLocation(&p, &m, &n, index);
                break;
            case 4:
                deleteElementFromEnd(&p, &m, &n);
                break;
            case 5:
                deleteElementFromBeginning(&p, &m, &n);
                break;
            case 6:
                printf("Enter the index to delete: ");
                scanf("%d", &index);
                deleteElementFromLocation(&p, &m, &n, index);
                break;
            case 7:
                sortStudents(p, m, compareRoll);
                printf("Array sorted by Roll.\n");
                break;
            case 8:
                sortStudents(p, m, compareCPI);
                printf("Array sorted by CPI.\n");
                break;
            case 9:
                printf("Students:\n");
                for (int i = 0; i < m; i++) {
                    printStudent(p[i]);
                }
                break;
            case 0:
                printf("Exiting program.\n");
                break;
            default:
                printf("Invalid choice. Try again.\n");
        }
    } while (choice != 0);

    // Free allocated memory
    for (int i = 0; i < m; i++) {
        free(p[i]->name);
        free(p[i]);
    }
    free(p);
}

*/
void main()
{
    Q1();
}
