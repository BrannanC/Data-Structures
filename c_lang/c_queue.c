#include <stdio.h>
#include <stdlib.h>

typedef struct Queue
{
    int front;
    int rear;
    int size;
    unsigned int capacity;
    int *data;
} Queue;

Queue *createQueue(unsigned int capacity)
{
    Queue *queue = malloc(sizeof(Queue));
    queue->capacity = capacity;
    queue->front = 0;
    queue->rear = 0;
    queue->size = 0;
    queue->data = malloc(capacity * sizeof(int));

    return queue;
}

int isFull(Queue *queue)
{
    return queue->size == queue->capacity;
}

int isEmpty(Queue *queue)
{
    return queue->size == 0;
}

void enqueue(Queue *queue, int item)
{
    if (isFull(queue))
    {
        queue->capacity *= 2;
        queue->data = realloc(queue->data, queue->capacity * sizeof(int));
    }
    queue->data[queue->rear++] = item;
    queue->size++;
}

int dequeue(Queue *queue)
{
    if (isEmpty(queue))
    {
        return -1;
    }
    queue->size--;
    return queue->data[queue->front++];
}

int main()
{
    Queue *queue = createQueue(4);

    printf("queue isFull: %d\n", isFull(queue));
    printf("queue isEmpty: %d\n", isEmpty(queue));

    enqueue(queue, 10);
    enqueue(queue, 20);
    enqueue(queue, 30);
    enqueue(queue, 40);

    printf("queue isFull: %d\n", isFull(queue));
    printf("isEmpty: %d\n", isEmpty(queue));

    printf("%d dequeued\n", dequeue(queue));
    printf("%d dequeued\n", dequeue(queue));
    printf("%d dequeued\n", dequeue(queue));
}