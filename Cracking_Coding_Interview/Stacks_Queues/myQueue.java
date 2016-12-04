// ben isenberg 9/17/2016
import java.util.*;

//implement a queue using 2 stacks
class myQueue
{
	Stack<Integer> stack1;

	public myQueue()
	{
		stack1 = new Stack<Integer>();
	}

	void enqueue(int a)
	{
		stack1.push(a);
	}

	int dequeue()
	{
		Stack<Integer> reverseStack = new Stack<Integer>();

		int len = stack1.size();

		// get first item added
		for (int x = 0; x < len; x++)
		{
			reverseStack.push(stack1.pop());
		}

		int item = reverseStack.pop();
		len = reverseStack.size();

		// reconstruct original stack
		for (int x = 0; x < len; x++)
		{
			stack1.push(reverseStack.pop());
		}

		return item;
	}

	int peek()
	{
		Stack<Integer> reverseStack = new Stack<Integer>();

		int len = stack1.size();

		// get first item added
		for (int x = 0; x < len; x++)
		{
			reverseStack.push(stack1.pop());
		}

		int item = reverseStack.peek();
		len = reverseStack.size();

		// reconstruct original stack
		for (int x = 0; x < len; x++)
		{
			stack1.push(reverseStack.pop());
		}

		return item;
	}

	public static void main(String[] args)
	{
		myQueue test = new myQueue();

		test.enqueue(1);
		test.enqueue(2);
		test.enqueue(6);
		test.enqueue(3);
		System.out.println("Peek " + test.peek());
		System.out.println("Dequeue " + test.dequeue());
		System.out.println("Peek " + test.peek());
		test.enqueue(4);
		System.out.println("Peek " + test.peek());
		System.out.println("Dequeue " + test.dequeue());
		System.out.println("Peek " + test.peek());
	}	
}