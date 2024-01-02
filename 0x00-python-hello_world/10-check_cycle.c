#include <stdlib.h>
#include "list.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: a singly linked list
 * return: 0 if there is no cycle
 * 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *apple, *orange;

	if (list == NULL || list->next == NULL)
		return (0);

	apple = list->next;
	orange = list->next->next;

	while (apple && orange && orange->next)
	{
		if (apple = orange)
			return (1);

		apple = apple->next;
		orange = orange->next->next;
	}
	return (0);
}
