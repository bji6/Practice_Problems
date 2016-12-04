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

	// remove duplicate values from unsorted linked list, n2 runtime but less memory intensive, no temporary buffer needed
	public static Node removeDuplicates(Node n)
	{
		int item;
		
		Node temp;  // temp pointer
		
		Node head = n; //head of linked list
		
		Node prev = n;  //node before temp pointer

		while (n != null)
		{
			item = n.data;

			temp = n.next;

			//System.out.println("inside loop 1: data = " + item);

			while (temp != null) // remove any duplicates of pointer N in the linked list
			{
				//System.out.println("inside loop 2: data = " + temp.data);

				if (item == temp.data)  //found a duplicate
				{
					System.out.println("found a match");
					//System.out.println("b4 temp " + temp.data + " temp.next " + temp.next.data);

					prev.next = temp.next;  // set previous node.next = temp node.next since temp is a duplicate
					temp = prev.next; // move temp to next node in list
					
					//System.out.println("after temp " + temp.data + " temp.next " + temp.next.data);
					continue;
					
				}
				//increment pointers
				temp = temp.next;  
				prev = prev.next;
			}
			
			n = n.next;  //increment n
			prev = n; //reset prev to n

		}

		return head;
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
		test.appendToTail(7);

		test.print();

		test = Node.removeDuplicates(test);

		test.print();
	}
}



