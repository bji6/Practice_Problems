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

	void appendNode(Node x)
	{
		Node n = this;
		while (n.next != null)
		{
			n = n.next;
		}
		n.next = x;	
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

	int length()
	{
		int len = 0;

		Node n = this;

		while (n != null)
		{
			len = len + 1;
			n = n.next;
		}

		return len;
	}

	//check if theres a loop in the linked list
	public static Node detectLoop(Node x)
	{
		Hashtable<String, Integer> node_map = new Hashtable<String, Integer>();

		String temp = "";

		while (x != null)
		{
			temp = temp + x;
			if (node_map.containsKey(temp))
			{
				System.out.println("Found circular reference at " + x);
				return x;
			}

			node_map.put(temp, 0);
			temp = "";
			x = x.next;
		}

		System.out.println("No circular reference");
		return null;
	}


	public static void main(String[] args)
	{
		Node test = new Node(7);
		test.appendToTail(1);
		test.appendToTail(6);
		test.appendToTail(1);
		test.appendToTail(7);

		Node test3 = new Node(5);
		test3.appendToTail(9);
		test3.appendToTail(1);
		test3.appendToTail(7);
		test3.appendNode(test3.next.next);

		Node.detectLoop(test);
		Node.detectLoop(test3);

		System.out.println(test3.next.next);
	}
}



