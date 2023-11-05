#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to head of list
 * @number: value of node
 * Return: address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *s;
	listint_t *current = *head;

	s = malloc(sizeof(listint_t));
	if (s == NULL)
		return (NULL);
	s->n = number;
	if (current == NULL || current->next->n >= number)
	{
		s->next = current;
		*head = s;
		return (s);
	}

	while (current && current->next && current->next->n < number)
		current = current->next;

	s->next = current->next;
	current->next = s;
	return (s);
}
