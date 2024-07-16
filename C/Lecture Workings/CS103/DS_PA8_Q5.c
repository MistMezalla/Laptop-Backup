#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

struct book_t 
{
    int ukey;        
    char *issn;    
    char *name;      
};

struct student_t 
{
    int roll;        
    char *name;
};

typedef union 
{
    struct book_t *book;
    struct student_t *student;
} Data;

typedef struct node 
{
    Data data;
    struct node *next;
} Node;

Node *new_node(Data data) 
{
    Node *node = (Node *)calloc(1,sizeof(Node));
    assert(node);
    node->data = data;
    node->next = NULL;
    return node;
}

void ins_pos_node(Node **head, Data data, int pos) 
{
    Node *node = new_node(data);

    if (pos == 0) {
        node->next = *head;
        *head = node;
        return;
    }

    Node *current = *head;
    int c = 0;

    while (current != NULL && c < pos - 1) 
    {
        current = current->next;
        c++;
    }

    if (current == NULL) {
        printf("Invalid position\n");
        return;
    }

    node->next = current->next;
    current->next = node;
}

void deleteNode(Node **head, int pos) 
{
    if (*head == NULL) 
    {
        printf("List is empty!\n");
        return;
    }

    if (pos == 0) {
        Node *temp = *head;
        *head = (*head)->next;
        free(temp);
        return;
    }

    Node *current = *head;
    int c = 0;

    while (current->next != NULL && c < pos - 1) 
    {
        current = current->next;
        c++;
    }

    if (current->next == NULL) {
        printf("Invalid position!\n");
        return;
    }

    Node *temp = current->next;
    current->next = temp->next;
    free(temp);
}

Data getNode(Node *head, int position) 
{
    Data data;
    data.book = NULL; 

    if (head == NULL) 
    {
        printf("List is empty!\n");
        return data;
    }

    Node *current = head;
    int c = 0;

    while (current != NULL && c < position) 
    {
        current = current->next;
        c++;
    }

    if (current == NULL) {
        printf("Invalid position!\n");
        return data;
    }

    return current->data;
}

int length(Node *head) 
{
    int len = 0;
    Node *current = head;
    while (current != NULL) 
    {
        len++;
        current = current->next;
    }
    return len;
}

void display(Node *head, void (*print)(Data)) 
{
    Node *current = head;
    while (current != NULL) 
    {
        print(current->data);
        current = current->next;
    }
}

void sortList(Node **head, int (*cmp)(Data, Data)) 
{
    if (*head == NULL || (*head)->next == NULL) 
    {
        return;  
    }

    Node *current = *head;
    Node *next_node = current->next;
    Node *sortedList = NULL;

    while (current != NULL) {
        next_node = current->next;
        ins_pos_node(&sortedList, current->data, 0);  
        current = next_node;
    }

    *head = sortedList;
}

void dis_Book(Data data) 
{
    printf("Book: ukey=%d, issn=%s, name=%s\n", data.book->ukey, data.book->issn, data.book->name);
}

void dis_Student(Data data) 
{
    printf("Student: roll=%d, name=%s\n", data.student->roll, data.student->name);
}

int comp_Book_Ukey(Data a, Data b) 
{
    return (a.book->ukey - b.book->ukey);
}

int comp_Student_Roll(Data a, Data b) 
{
    return (a.student->roll - b.student->roll);
}

int main() 
{
    Node *book_List = NULL;
    struct book_t book1 = {101, "ISSN001", "Book A"};
    struct book_t book2 = {107, "ISSN007", "Book B"};
    Data bookData1, bookData2;
    bookData1.book = &book1;
    bookData2.book = &book2;

    ins_pos_node(&book_List, bookData1, 0);
    ins_pos_node(&book_List, bookData2, 1);

    sortList(&book_List, comp_Book_Ukey);
    printf("List of books (sorted by ukey):\n");
    display(book_List, dis_Book);

    Node *student_List = NULL;
    struct student_t student1 = {89, "Harshal"};
    struct student_t student2 = {101, "Junaid"};
    Data studentData1, studentData2;
    studentData1.student = &student1;
    studentData2.student = &student2;

    ins_pos_node(&student_List, studentData1, 0);
    ins_pos_node(&student_List, studentData2, 1);

    sortList(&student_List, comp_Student_Roll);
    printf("\nList of students (sorted by roll):\n");
    display(student_List, dis_Student);

    return 0;
}
