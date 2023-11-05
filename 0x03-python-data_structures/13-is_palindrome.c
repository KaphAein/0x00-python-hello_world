#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
#include <stddef.h>
/**
 * reverse_listint - reverses a list
 * @head: pointer to head of list
 * Return: pointer to the first node in the new list
 */
void reverse_listint(listint_t **head)
{
	listint_t *prev = NULL, *current = *head, *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}


/**
 * is_palindrome - checks if list is palindrome
 * @head: pointer to head of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast = *head, *slow = *head, *cop = NULL, *current = *head;


	if (*head == NULL && (*head)->next == NULL)
	{
		return (1);
	}
	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			cop = slow->next;
			break;
		}
		if (!fast->next)
		{
			cop = slow->next->next;
			break;
		}
		slow = slow->next;
	}
	reverse_listint(&cop);
	while (cop && current)
	{
		if (cop->n == current->n)
		{
			cop = cop->next;
			current = current->next;
		}
		else
			return (0);
	}
	if (!cop)
		return (1);
	return (0);
}
