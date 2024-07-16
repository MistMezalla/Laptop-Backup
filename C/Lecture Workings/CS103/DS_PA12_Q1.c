#include <stdio.h>
#include <stdlib.h>

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

    undirected_graph_matrix* undirected_graph_matrix = create_undirected_graph_matrix(nv, ne, edges);
    print_adj_matrix(undirected_graph_matrix->adj_matrix, nv);

    directed_graph_matrix* directed_graph_matrix = create_directed_graph_matrix(nv, ne, edges);
    print_adj_matrix(directed_graph_matrix->adj_matrix, nv);

    undirected_graph_list* undirected_graph_list = create_undirected_graph_list(nv, ne, edges);
    print_adj_list(undirected_graph_list->adj_list, nv);

    directed_graph_list* directed_graph_list = create_directed_graph_list(nv, ne, edges);
    print_adj_list(directed_graph_list->adj_list, nv);
}
