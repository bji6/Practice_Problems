// ben isenberg 9/17/2016
import java.util.*;

//Class represents a set of stacks that have a max capacity
class SetOfStacks
{
	ArrayList<Stack> stackList;
	int max_capacity;
	int stack_count;

	public SetOfStacks(int x)
	{
		stackList = new ArrayList<Stack>();
		max_capacity = x;
		stack_count = 0;
	}

	void push(int x)
	{
		if (stack_count == 0)
		{
			Stack<Integer> mystack = new Stack<Integer>();
			stackList.add(stack_count, mystack);
			stack_count = stack_count + 1;
		}

		Stack<Integer> mystack = stackList.get(stack_count-1);

		//need to make a new stack if at full capacity
		if (mystack.size() == max_capacity)
		{
			mystack = new Stack<Integer>();
			mystack.push(x);
			stackList.add(stack_count, mystack);
			stack_count = stack_count + 1;
		}
		else
		{
			mystack.push(x);
		}
	}

	int pop()
	{
		if (stack_count == 0)
		{
			System.out.println("Empty stack");
			return -999;
		}
	
		Stack<Integer> mystack = stackList.get(stack_count-1);
		int x = mystack.pop();

		if (mystack.size() == 0)
		{
			stack_count = stack_count - 1;
		}

		System.out.println("Popped " + x);
		return x;
	}

	//this function lets you pick which stack to pop from
	/*would need to rebalance stacks since this can create 
	wasted space*/
	int popAt(int index)
	{
		if (index > stack_count)
		{
			System.out.println("Stack doesnt exist");
			return -999;
		}

		if (stack_count == 0)
		{
			System.out.println("Empty stack");
			return -999;
		}
	
		Stack<Integer> mystack = stackList.get(index-1);
		int x = mystack.pop();

		System.out.println("Popped " + x);
		return x;	
	}

	int peek()
	{
		if (stack_count == 0)
		{
			System.out.println("Empty stack");
			return -999;
		}

		Stack<Integer> mystack = stackList.get(stack_count-1);

		System.out.println("Peeked " + mystack.peek());
		return mystack.peek();
	}	

	public static void main(String[] args)
	{
		SetOfStacks test = new SetOfStacks(3);

		test.peek();
		test.pop();

		test.push(1);
		test.push(2);
		test.push(6);
		test.push(3);
		test.peek();
		test.pop();
		test.peek();
		test.push(4);
		test.push(88);
		test.push(66);
		test.peek();
		test.pop();
		test.peek();
		test.popAt(1);
		test.peek();
	}
}