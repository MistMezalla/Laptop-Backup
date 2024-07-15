#include <bits/stdc++.h>
using namespace std;

class Node
{
    public:
        int data;
        Node *next,*prev;

    Node()
    {
        data = 0;
        next = prev = NULL;
    }
    Node (int data,Node *next=NULL,Node *prev=NULL)
    {
        this->data=data;
        this->next = next;
        this->prev = prev;
    }
};

class Doubly_Linked_list
{
    public:
        Node *head;
        Node *tail;
    
        void ins_at_st(int data);

        void print_for();

        void print_back();

        void ins_at_end(int data);

        int length();

        void ins_at_pos(int data,int pos);

        void ins_bef_val(int data,int val);

        void ins_aft_val(int data);

        void del_st();

        void del_end();

        void del_bef_val();

        void del_aft_val();

        void del_at_pos();

        void rev_list();

    Doubly_Linked_list()
    {
        head = NULL;
        tail = NULL;
    }
};

void Doubly_Linked_list::ins_at_st(int data)
{
    if (head == NULL)
    {
        Node *new_node = new Node(data);
        head = new_node;
        tail = new_node;
        return;
    }

    Node *new_node= new Node(data,head);
    head->prev=new_node;
    head = new_node;

    if (head->next)
    cout << head->next->data << endl;
    if (head->prev)
    cout << head->prev->data << endl;
}

void Doubly_Linked_list::print_for()
{
    if (head == NULL)
    {
        cout << "Empty List" << endl;
        return;
    }

    Node *ptr=head;

    cout << "Forward:-" << endl;
    while(ptr)
    {
        cout << "<--" << ptr->data << "-->" ;
        ptr=ptr->next;
    }
    cout << endl;
}

void Doubly_Linked_list::print_back()
{
    if (tail == NULL)
    {
        cout << "Empty List" << endl;
        return;
    }

    Node *ptr = tail;

    cout << "Backward:-" << endl;
    while(ptr)
    {
        cout << "<--" << ptr->data << "-->" ;
        ptr=ptr->prev;   
    }
    cout << endl;
}

void Doubly_Linked_list::ins_at_end(int data)
{
    if (tail == NULL)
    {
        Node *new_node= new Node(data);
        tail = new_node;
        head = new_node;
        return;
    }

    Node *new_node = new Node(data,NULL,tail);
    tail->next=new_node;
    tail=new_node;
}

int Doubly_Linked_list::length()
{
    Node *ptr = head;
    int cnt = 0;
    while(ptr)
    {
        cnt++;
        ptr=ptr->next;
    }
    return cnt;
}

void Doubly_Linked_list::ins_at_pos(int data,int pos)
{
    if (pos>=length())
    {
        cout<< "Out of bound error" <<endl;
        return;
    }

    if (pos==0)
    {
        ins_at_st(data);
        return;
    }

    Node *ptr = head;
    int cnt=0;
    while (cnt!=pos-1)
    {
        ptr=ptr->next;
        cnt++;
    }

    Node *new_node= new Node(data,ptr->next->next,ptr);
    ptr->next->next->prev=new_node;
    ptr->next=new_node;

    if (new_node->next == NULL) 
    {
        tail = new_node;
    }

}

void Doubly_Linked_list::ins_bef_val(int data,int val)
{
    Node *ptr = head;

    if (ptr->data==val)
    {
        ins_at_st(data);
        return;
    }

    
    try
    {
        while(ptr->next != NULL && ptr->next->data != val)
        {
        ptr=ptr->next;
        }

        Node *new_node= new Node(data,ptr->next->next,ptr);
        ptr->next->next->prev=new_node;
        ptr->next=new_node;

        if (new_node->next == NULL) 
        {
        tail = new_node;
        }
    }
    catch(const exception& e)
    {
        cout << typeid(e).name() << ": Value not found";
    }
    

}

void Doubly_Linked_list::del_st()
{
    if (!head)
    {
        cout << "Empty List" <<endl;
        return;
    }

    if (head ==  tail)
    {
        Node *ptr = head;
        head = tail = NULL;
        delete ptr;
        return;
    }

    Node *ptr = head;
    head->next->prev=NULL;
    head = head->next;

    delete ptr;
}

void Doubly_Linked_list::del_end()
{
    if (!tail)
    {
        cout << "empty List" << endl;
        return;
    }

    if (head ==  tail)
    {
        Node *ptr = head;
        head = tail = NULL;
        delete ptr;
        return;
    }

    Node *ptr = tail;
    tail->prev->next=NULL;
    tail = tail->prev;

    delete ptr;
}

void Doubly_Linked_list::rev_list()
{
    Node *ptr = head;
    while(ptr)
    {
        swap(ptr->next,ptr->prev);
        ptr=ptr->prev;
    }
    swap(head,tail);
}

int main()
{
    Doubly_Linked_list list;

    list.ins_at_st(10);
    list.print_for();
    list.print_back();

    list.ins_at_st(20);
    list.print_for();
    list.print_back();

    list.ins_at_st(30);
    list.print_for();
    list.print_back();

    list.ins_at_end(40);
    list.print_for();
    list.print_back();

    cout << list.length() << endl;
    list.ins_at_pos(57,2);
    list.print_for();
    list.print_back();

    list.del_st();
    list.del_end();
    list.print_for();
    list.print_back();

    list.rev_list();
    list.print_for();
    list.print_back();

    Doubly_Linked_list List;
    List.ins_at_end(20);
    List.ins_bef_val(30,20);
    List.print_for();
    List.print_back();
    List.ins_bef_val(0,40);
    List.print_for();
    List.print_back();

    
    return 0;
}