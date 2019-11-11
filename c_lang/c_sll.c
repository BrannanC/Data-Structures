#include <stdlib.h>
#include <stdio.h>

typedef struct Node
{
    struct Node *next;
    int value;
} Node;

typedef struct LinkedList
{
    Node *head;
    Node *tail;
    int size;
} LinkedList;

LinkedList *create_list(void)
{
    LinkedList *ll = malloc(sizeof(LinkedList));
    ll->head = NULL;
    ll->tail = NULL;
    ll->size = 0;

    return ll;
}

void free_list(LinkedList *ll)
{
    if (ll)
    {
        free(ll);
    }
}

Node *create_node(int value, Node *next)
{
    Node *node = malloc(sizeof(Node));
    node->value = value;
    node->next = next;

    return node;
}

void free_node(Node *node)
{
    if (node)
    {
        free(node);
    }
}

void add_to_tail(LinkedList *ll, int value)
{
    Node *new_node = create_node(value, NULL);
    ll->tail->next = new_node;
    ll->tail = new_node;
    ll->size++;
}

Node *list_search(LinkedList *ll, int target)
{
    Node *current = ll->head;

    while (current)
    {
        if (current->value == target)
        {
            return current;
        }
        current = current->next;
    }

    return NULL;
}

void list_delete(LinkedList *ll, int target)
{
    int found = 0;
    Node *prev = NULL;
    Node *curr = ll->head;

    while (curr && !found)
    {
        if (curr->value == target)
        {
            found = 1;
        }
        else
        {
            prev = curr;
            curr = curr->next;
        }
    }
    if (prev == NULL && found)
    {
        Node *node_to_delete = ll->head;
        ll->head = curr->next;
        free_node(node_to_delete);
        ll->size--;
    }
    else if (found && curr)
    {
        Node *node_to_delete = curr;
        prev->next = curr->next;
        free_node(node_to_delete);
        ll->size--;
    }
}

int main(void)
{
    return 0;
}