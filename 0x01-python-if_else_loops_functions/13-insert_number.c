#include "lists.h"
/**
 * 
*/
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *tmp, *newNode;
    if(head == NULL || *head == NULL)
    {
        newNode = malloc(sizeof(listint_t) + 1);
        newNode->n = number;
        newNode->next = NULL;
        *head = newNode;
    }
    else
    {
    tmp = *head;
    while(tmp)
    {
        if(tmp->next->n > number)
            break;
        else
            tmp = tmp->next;
    }
    newNode = malloc(sizeof(listint_t) + 1);
    newNode->n = number;
    newNode->next = tmp->next;
    tmp->next = newNode;
    }
    return (*head);
}
