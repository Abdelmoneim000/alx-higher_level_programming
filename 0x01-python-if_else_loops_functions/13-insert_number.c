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
    newNode = malloc(sizeof(listint_t));
    newNode->n = number;
    tmp = *head;
    while(tmp->next)
    {
        if(tmp->n > newNode->n && tmp == *head)
        {
            newNode->next = tmp;
            *head = newNode;

            return (*head);
        }
        else if(tmp->next->n > number)
        {
            newNode->next = tmp->next;
            tmp->next = newNode;

            return (*head);
        }
        else
            tmp = tmp->next;
    }
    tmp->next = newNode;
    }
    return (*head);
}
