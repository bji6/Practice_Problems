/* Ben Isenberg 9/10/2016 */

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct Element {
	struct Element *next;
	int data;
} Element;

/*pass in ptr of ptr so that stack modification exists 
outside function */
bool push(Element **stack, int data);

/*pass in ptr of ptr so that stack modification exists 
outside function */
bool pop(Element **stack);

bool push(Element **stack, int data)
{
	if (stack != NULL)
	{
		Element *item = malloc(sizeof(Element));  /* create a new node */

		item->data = data;  /* set data */

		item->next = *stack; /*new node->next points to top of stack */

		*stack = item;  /*stack ptr points to new node now */

		return true;
	}
	
	return false;
}

bool pop(Element **stack)
{
	if (stack != NULL)	/*check for null ptr*/
	{
		Element *temp = (*(stack))->next; /*dereference ptr of ptr and set temp to point to element->next*/

		free(*stack);  /*dereference ptr of ptr, and free what that ptr points to*/

		*stack = temp; /*dereference ptr of ptr, and have that ptr point to what temp points to*/

		return true;
	}

	return false;
}

void printStack(Element *stack)
{
	Element *temp = stack;

	while (temp != NULL || temp->next != NULL)
	{
		printf("%d\n", temp->data);
		temp = temp->next;
	}

	printf("\n");

}



int main()
{
	printf("Does this work?\n");
	
	Element *stack = malloc(sizeof(Element));

	//int * number = malloc(sizeof(int));

	int number = 7;

	//pass address of stack ptr, not stack data
	push(&stack, number);
	push(&stack, 6);
	push(&stack, 5);

	printStack(stack);

	pop(&stack);
	printStack(stack);
	pop(&stack);
	printStack(stack);
	pop(&stack);
	printStack(stack);

	push(&stack, 14);
	printStack(stack);	

	return 0;
}