#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: If there is no cycle - 0.
 *         If there is a cycle - 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *apple, *pear;

	if (list == NULL || list->next == NULL)
		return (0);

	apple = list->next;
	pear = list->next->next;

	while (apple && pear && pear->next)
	{
		if (apple == pear)
			return (1);

		apple = apple->next;
		pear = pear->next->next;
	}

	return (0);
}
