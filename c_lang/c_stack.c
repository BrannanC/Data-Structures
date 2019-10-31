#include <stdio.h>
#include <stdlib.h>

typedef struct Stack
{
    int top;
    unsigned int capacity;
    int *data;
} Stack;

Stack *createStack(unsigned int capacity)
{
    Stack *stack = malloc(sizeof(struct Stack));
    stack->capacity = capacity;
    stack->top = -1;
    stack->data = malloc(capacity * sizeof(int));
    return stack;
}

int isFull(Stack *stack)
{
    return stack->top == stack->capacity - 1;
}

int isEmpty(Stack *stack)
{
    return stack->top == -1;
}

void push(Stack *stack, int item)
{
    if (isFull(stack))
    {
        stack->capacity *= 2;
        stack->data = realloc(stack->data, stack->capacity * sizeof(int));
    }

    stack->data[++stack->top] = item;
}

int pop(Stack *stack)
{
    if (isEmpty(stack))
    {
        return -1;
    }

    return stack->data[stack->top--];
}

int main()
{
    Stack *stack = createStack(2);

    printf("stack isFull: %d\n", isFull(stack));
    printf("stack isEmpty: %d\n", isEmpty(stack));

    push(stack, 10);
    push(stack, 20);
    printf("stack isFull: %d\n", isFull(stack));
    printf("isEmpty: %d\n", isEmpty(stack));

    printf("%d popped\n", pop(stack));
    printf("%d popped\n", pop(stack));
    printf("%d popped\n", pop(stack));

    int push_count = 100000;
    for (int i = 0; i < push_count; i++)
    {
        push(stack, i);
    }

    for (int i = push_count - 1; i >= 0; i--)
    {
        int v = pop(stack);

        if (v != i)
        {
            printf("Expected %d but got %d\n", v, i);
        }
    }

    return 0;
}