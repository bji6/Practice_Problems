// ben isenberg 9/17/2016
import java.util.*;

//sort a stack using 2 stacks
class sortedStack
{
	Stack<Integer> stack1;

	public sortedStack()
	{}

	void sortStack(Stack<Integer> s)
	{
		stack1 = s;

		Stack<Integer> stack2 = new Stack<Integer>();
		int min;

		while (stack1.empty() == false)
		{
			min = stack1.pop();
			if (stack2.empty())
			{
				stack2.push(min);
				continue;
			}

			while (stack2.empty() == false)
			{
				if (stack2.peek() > min)
				{
					stack1.push(stack2.pop());
					
					if (stack2.empty())
					{
						stack2.push(min);
						break;
					}
				}
				else
				{
					stack2.push(min);
					break;
				}
			}
		}

		stack1 = stack2;
	}

	void printStack()
	{
		Stack<Integer> temp = new Stack<Integer>();

		while (stack1.empty() == false)
		{
			temp.push(stack1.pop());
			System.out.println(temp.peek());
		}

		//rebuild original stack
		while (temp.empty() == false)
		{
			stack1.push(temp.pop());
		}
	}

	public static void main(String[] args)
	{
		sortedStack test = new sortedStack();

		Stack<Integer> mystack = new Stack<Integer>();

		mystack.push(3);
		mystack.push(7);
		mystack.push(2);
		mystack.push(8);

		test.sortStack(mystack);

		test.printStack();
	}	
}