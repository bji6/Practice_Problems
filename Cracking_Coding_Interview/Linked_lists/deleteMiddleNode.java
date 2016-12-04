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
			System.out.println();
	}

	//delete middle node, given only access to that node
	public static void deleteMiddle(Node n)
	{
		if (n == null || n.next == null)
		{
			return;
		}

		int count = 0;
		Node prev = n;

		while (n.next != null)
		{
			n.data = n.next.data;
			
			if (count > 0)
			{
				prev = n;
			}

			n = n.next;

			count = count + 1;
		}

		prev.next = n.next;

		return;
	}


	public static void main(String[] args)
	{
		Node test = new Node(7);

		test.appendToTail(3);
		test.appendToTail(4);
		test.appendToTail(230);
		test.appendToTail(6);
		test.appendToTail(5);
		test.appendToTail(7);
		test.appendToTail(14);

		test.print();

		Node.deleteMiddle(test.next.next.next);

		test.print();
	}
}



