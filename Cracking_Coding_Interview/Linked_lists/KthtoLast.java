// ben isenberg 9/17/2016

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
	}

	//return kth to last element of singly linked list
	public static int kthToLast(Node n, int k)
	{
		Node head = n;
		Node prev = n;

		for (int x = 0; x < k; x++)
		{
			if (head == null)
			{
				System.out.printf("Error, list length < %d \n", k);
				return -9999;
			}

			head = head.next;
		}

		if (k == 0) //so we print last node correctly
		{
			head = head.next;	
		}

		while (head != null)
		{
			head = head.next;
			prev = prev.next;
		}

		return prev.data;
	}


	public static void main(String[] args)
	{
		Node test = new Node(7);

		test.appendToTail(3);
		test.appendToTail(4);
		test.appendToTail(3);
		test.appendToTail(3);
		test.appendToTail(3);
		test.appendToTail(5);
		test.appendToTail(4);
		test.appendToTail(14);

		test.print();

		System.out.printf("%d th to last = %d\n", 3, Node.kthToLast(test, 3));
		System.out.printf("%d th to last = %d\n", 5, Node.kthToLast(test, 5));
		System.out.printf("%d th to last = %d\n", 10, Node.kthToLast(test, 10));
		System.out.printf("%d th to last = %d\n", 9, Node.kthToLast(test, 9));
		System.out.printf("%d th to last = %d\n", 0, Node.kthToLast(test, 0));

		test.print();
	}
}



