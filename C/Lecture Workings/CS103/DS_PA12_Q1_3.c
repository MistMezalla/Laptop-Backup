#include <stdio.h>
#include <stdlib.h>

typedef struct queue
{
    int front, rear, size;
    int capacity;
    int* array;
}queue;

queue* create_queue(int capacity)
{
    queue* q = (queue*)malloc(sizeof(queue));
    q->capacity = capacity;
    q->front = q->size = 0;
    q->rear = capacity - 1;
    q->array = (int*)malloc(q->capacity * sizeof(int));
    return q;
}

int is_full(queue* q)
{
    return (q->size == q->capacity);
}

int is_empty(queue* q)
{
    return (q->size == 0);
}

void enqueue(queue* q, int item)
{
    if (is_full(q))
        return;
    q->rear = (q->rear + 1) % q->capacity;
    q->array[q->rear] = item;
    q->size = q->size + 1;
}

int dequeue(queue* q)
{
    if (is_empty(q))
        return -1;
    int item = q->array[q->front];
    q->front = (q->front + 1) % q->capacity;
    q->size = q->size - 1;
    return item;
}

int front(queue* q)
{
    if (is_empty(q))
        return -1;
    return q->array[q->front];
}

int rear(queue* q)
{
    if (is_empty(q))
        return -1;
    return q->array[q->rear];
}

typedef struct 
{
    int nv;
    int **adj_matrix;
} undirected_graph_matrix;

typedef struct 
{
    int nv;
    int **adj_matrix;
} directed_graph_matrix;

typedef struct adj_list_node 
{
    int vertex;
    struct adj_list_node* next;
} adj_list_node;

typedef struct 
{
    int nv;
    adj_list_node **adj_list;
} undirected_graph_list;

typedef struct 
{
    int nv;
    adj_list_node **adj_list;
} directed_graph_list;

undirected_graph_matrix* create_undirected_graph_matrix(int nv, int ne, int edges[][2]) 
{
    undirected_graph_matrix* graph = (undirected_graph_matrix*)malloc(sizeof(undirected_graph_matrix));
    graph->nv = nv;
    graph->adj_matrix = (int**)malloc(nv * sizeof(int*));
    int i;
    for (i = 0; i < nv; i++) 
    {
        graph->adj_matrix[i] = (int*)calloc(nv, sizeof(int));
    }
    for (i = 0; i < ne; i++) 
    {
        int u = edges[i][0];
        int v = edges[i][1];
        graph->adj_matrix[u][v] = 1;
        graph->adj_matrix[v][u] = 1;
    }
    return graph;
}

directed_graph_matrix* create_directed_graph_matrix(int nv, int ne, int edges[][2]) 
{
    directed_graph_matrix* graph = (directed_graph_matrix*)malloc(sizeof(directed_graph_matrix));
    graph->nv = nv;
    graph->adj_matrix = (int**)malloc(nv * sizeof(int*));
    int i;
    for (i = 0; i < nv; i++) 
    {
        graph->adj_matrix[i] = (int*)calloc(nv, sizeof(int));
    }
    for (i = 0; i < ne; i++) 
    {
        int u = edges[i][0];
        int v = edges[i][1];
        graph->adj_matrix[u][v] = 1;
    }
    return graph;
}

undirected_graph_list* create_undirected_graph_list(int nv, int ne, int edges[][2]) 
{
    undirected_graph_list* graph = (undirected_graph_list*)malloc(sizeof(undirected_graph_list));
    graph->nv = nv;
    graph->adj_list = (adj_list_node**)malloc(nv * sizeof(adj_list_node*));
    int i;
    for (i = 0; i < nv; i++) 
    {
        graph->adj_list[i] = NULL;
    }
    for (i = 0; i < ne; i++) 
    {
        int u = edges[i][0];
        int v = edges[i][1];
        adj_list_node* new_node = (adj_list_node*)malloc(sizeof(adj_list_node));
        new_node->vertex = v;
        new_node->next = graph->adj_list[u];
        graph->adj_list[u] = new_node;
        new_node = (adj_list_node*)malloc(sizeof(adj_list_node));
        new_node->vertex = u;
        new_node->next = graph->adj_list[v];
        graph->adj_list[v] = new_node;
    }
    return graph;
}

directed_graph_list* create_directed_graph_list(int nv, int ne, int edges[][2]) 
{
    directed_graph_list* graph = (directed_graph_list*)malloc(sizeof(directed_graph_list));
    graph->nv = nv;
    graph->adj_list = (adj_list_node**)malloc(nv * sizeof(adj_list_node*));
    int i;
    for (i = 0; i < nv; i++) 
    {
        graph->adj_list[i] = NULL;
    }
    for (i = 0; i < ne; i++) 
    {
        int u = edges[i][0];
        int v = edges[i][1];
        adj_list_node* new_node = (adj_list_node*)malloc(sizeof(adj_list_node));
        new_node->vertex = v;
        new_node->next = graph->adj_list[u];
        graph->adj_list[u] = new_node;
    }
    return graph;
}

void print_adj_matrix(int** matrix, int nv) 
{
    printf("Adjacency Matrix:\n");
    int i,j;
    for (i = 0; i < nv; i++) 
    {
        for (j = 0; j < nv; j++) 
        {
            printf("%d ", matrix[i][j]);
        }
        printf("\n");
    }
}

void print_adj_list(adj_list_node** adj_list, int nv) 
{
    printf("Adjacency List:\n");
    int i;
    for (i = 0; i < nv; i++) {
        printf("Vertex %d: ", i);
        adj_list_node* current = adj_list[i];
        while (current != NULL) {
            printf("%d ", current->vertex);
            current = current->next;
        }
        printf("\n");
    }
}

void bfs(directed_graph_list* graph, int start) 
{
    queue* queue = create_queue(graph->nv);
    int* visited = (int*)calloc(graph->nv, sizeof(int));
    visited[start] = 1;
    enqueue(queue, start);

    while (!is_empty(queue)) 
    {
        int current_vertex = dequeue(queue);
        printf("%d ", current_vertex);

        adj_list_node* temp = graph->adj_list[current_vertex];
        while (temp != NULL) 
        {
            int adj_vertex = temp->vertex;
            if (!visited[adj_vertex]) 
            {
                visited[adj_vertex] = 1;
                enqueue(queue, adj_vertex);
            }
            temp = temp->next;
        }
    }

    free(visited);
    free(queue);
}

void dfs(adj_list_node** adj_list, int start, int* visited) 
{
    printf("%d ", start);
    visited[start] = 1;

    adj_list_node* temp = adj_list[start];
    while (temp != NULL) 
    {
        int adj_vertex = temp->vertex;
        if (!visited[adj_vertex]) 
        {
            dfs(adj_list, adj_vertex, visited);
        }
        temp = temp->next;
    }
}

void main() 
{
    int nv, ne;
    printf("Enter the number of vertices and edges: ");
    scanf("%d %d", &nv, &ne);

    int edges[ne][2];
    printf("Enter the edges as pairs of vertices (i, j):\n");
    int i;
    for (i = 0; i < ne; i++) 
    {
        scanf("%d %d", &edges[i][0], &edges[i][1]);
    }

    //Graph
    undirected_graph_matrix* undirected_graph_matrix = create_undirected_graph_matrix(nv, ne, edges);
    print_adj_matrix(undirected_graph_matrix->adj_matrix, nv);

    directed_graph_matrix* directed_graph_matrix = create_directed_graph_matrix(nv, ne, edges);
    print_adj_matrix(directed_graph_matrix->adj_matrix, nv);

    undirected_graph_list* undirected_graph_list = create_undirected_graph_list(nv, ne, edges);
    print_adj_list(undirected_graph_list->adj_list, nv);

    directed_graph_list* directed_graph_list = create_directed_graph_list(nv, ne, edges);
    print_adj_list(directed_graph_list->adj_list, nv);

    //BFS traversal
    int start_vertex;
    printf("Enter the starting vertex for BFS traversal: ");
    scanf("%d", &start_vertex);

    printf("BFS Traversal starting from vertex %d: ", start_vertex);
    bfs(directed_graph_list, start_vertex);
    printf("\n");

    // DFS traversal
    printf("Enter the starting vertex for DFS traversal: ");
    scanf("%d", &start_vertex);

    printf("DFS Traversal starting from vertex %d: ", start_vertex);
    int* visited_dfs = (int*)calloc(nv, sizeof(int)); 
    dfs(directed_graph_list->adj_list, start_vertex, visited_dfs);
    printf("\n");
    free(visited_dfs); 

}
