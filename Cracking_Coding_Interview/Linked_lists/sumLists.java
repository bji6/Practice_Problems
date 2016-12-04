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

	//add digits in a linked list, digits in reverse order
	//recursive method
	public static Node addLists(Node x, Node y, int overflow)
	{
		int data1 = x.data;
		int data2 = y.data;

		int sum = data1 + data2 + overflow;

		int overflow2 =  sum / 10;  //overflow amount, integer division

		Node newNode = new Node(sum % 10);  // new node with data

		if (x.next == null && y.next == null)
		{
			if (overflow2 < 1)
			{
				return newNode;
			}
			else
			{
				Node newNode2 = new Node(overflow2);
				newNode.next = newNode2;

				return newNode;
			}

		}
		else if (x.next == null && y.next != null)
		{
			newNode.next = Node.addLists(new Node(0),y.next,overflow2);

			return newNode;
		}
		else if (x.next != null && y.next == null)
		{
			newNode.next = Node.addLists(x.next,new Node(0),overflow2);

			return newNode;
		}

		newNode.next = Node.addLists(x.next,y.next,overflow2);

		return newNode;
	}


	public static void main(String[] args)
	{
		Node test = new Node(7);
		test.appendToTail(1);
		test.appendToTail(6);
		test.appendToTail(4);
		test.appendToTail(8);

		Node test2 = new Node(5);
		test2.appendToTail(9);
		test2.appendToTail(4);

		Node test3 = Node.addLists(test,test2,0);

		test3.print();

		test = new Node(9);
		test.appendToTail(7);
		test.appendToTail(8);

		test2 = new Node(6);
		test2.appendToTail(8);
		test2.appendToTail(5);

		test3 = Node.addLists(test,test2,0);

		test3.print();
	}
}



