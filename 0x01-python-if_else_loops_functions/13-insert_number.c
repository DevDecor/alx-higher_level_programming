#include "lists.h"
/**
 * insert_node - Inserts a node in a sorted list
 * @head: head node of the list
 * @number: valuse to be inserted
 * Return: new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *buff = *head, *new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (*head == NULL)
		return (new);
	if (buff->n > number)
	{
		new->next = buff;
		*head = new;
		return (new);
	}
	while (buff->next != NULL)
	{
		if (buff->next->n > number)
		{
			new->next = buff->next;
			buff->next = new;
			return (new);
		}
		buff = buff->next;
	}
	new->next = buff->next;
	buff->next = new;
	return (new);
}
