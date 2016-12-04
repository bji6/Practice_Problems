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
	public static void partitionList(Node n, int x)
	{
		if (n == null || n.next == null)
		{
			return;
		}

		Node temp;

		while (n != null)
		{
			temp = n.next;

			if (n.data >= x)
			{
				while (temp != null)
				{
					if (temp.data < x)  //perform swap
					{
						int item = temp.data;
						temp.data = n.data;
						n.data = item;
						break;
					}
					temp = temp.next;
				}
			}

			n = n.next;
		}

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

		Node.partitionList(test, 8);

		test.print();
	}
}



