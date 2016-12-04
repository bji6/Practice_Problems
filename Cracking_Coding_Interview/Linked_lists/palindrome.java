// ben isenberg 9/17/2016
import java.util.*;

//linked list class
class Node 
{
	Node next = null;
	int data;

	public Node(int d)
	{
		data = d;
	}

	void appendToTail(int d)
	{
		Node end = new Node(d);
		Node n = this;
		while (n.next != null)
		{
			n = n.next;
		}
		n.next = end;
	}

	void print()
	{
		Node n = this;
		while (n != null)
		{
			System.out.println(n.data);
			n = n.next;
		}
			System.out.println();
	}

	//check if a linked list is a palindrome, with the help of a stack
	public static void checkPalindrome(Node x)
	{
		Stack<Integer> mystack = new Stack<Integer>();
		Node temp = x;

		while (temp != null)
		{
			mystack.push(new Integer(temp.data));
			temp = temp.next;
		}

		//check if palindrome
		while (x != null)
		{
			int item = (int) mystack.pop();

			if (x.data != item)
			{
				System.out.println("List is NOT a palindrome");
				return;
			}
			x = x.next;
		}

		System.out.println("List is a palindrome");
	}


	public static void main(String[] args)
	{
		Node test = new Node(7);
		test.appendToTail(1);
		test.appendToTail(6);
		test.appendToTail(1);
		test.appendToTail(7);

		Node test2 = new Node(5);
		test2.appendToTail(9);
		test2.appendToTail(4);
		test2.appendToTail(5);

		Node.checkPalindrome(test);
		Node.checkPalindrome(test2);
	}
}



