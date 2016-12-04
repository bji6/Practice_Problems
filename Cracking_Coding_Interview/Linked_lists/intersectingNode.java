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

	//check two linked lists have intersecting nodes, return the node
	public static Node checkIntersect(Node x, Node y)
	{
		int lenx = x.length();
		int leny = y.length();
		Node temp;

		if (lenx > leny)
		{
			int diff = lenx - leny;
			int count = 0;
			temp = y;

			while (x != null)
			{
				if (count >= diff)
				{
					while (y != null)
					{
						System.out.println("Node x = " + x);
						System.out.println("Node y = " + y);
						if (x == y)
						{
							System.out.println("Intersecting Node = " + y);
							return x;
						}
						y = y.next;
					}
				}				
				x = x.next;
				y = temp;
				count = count + 1;
			}
		}
		else
		{
			int diff = leny - lenx;
			int count = 0;
			temp = x;

			while (y != null)
			{
				if (count >= diff)
				{
					while (x != null)
					{
						System.out.println("Node x = " + x);
						System.out.println("Node y = " + y);
						if (x == y)
						{
							System.out.println("Intersecting Node = " + y);
							return x;
						}
						x = x.next;
					}
				}				
				y = y.next;
				x = temp;
				count = count + 1;
			}
		}
		System.out.println("No intersection!\n");
		return null;
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

		Node test3 = new Node(5);
		test3.appendToTail(9);
		test3.appendNode(test.next.next);

		Node.checkIntersect(test,test2);
		Node.checkIntersect(test,test3);
	}
}



