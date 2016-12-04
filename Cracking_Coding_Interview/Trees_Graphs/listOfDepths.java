// ben isenberg 9/24/2016
import java.util.*;

class Node
{
	public Node left_child;
	public Node right_child;
	public int data;

	public Node(int n)
	{
		data = n;
	}

	public void setLeftNode(Node x)
	{
		left_child = x;
	}

	public void setRightNode(Node x)
	{
		right_child = x;
	}

	public Node getLeftNode()
	{
		return left_child;
	}

	public Node getRightNode()
	{
		return right_child;
	}

	//bfs traversal of a binary tree, iterative
	//create linked list of nodes at each depth
	public static ArrayList<LinkedList<Node>> bfsTraversal(Node head)
	{
		// java linkedlist implements Queue interface
		LinkedList<Node> myqueue = new LinkedList<Node>();
		myqueue.add(head);

		int number_of_children = 0;
		int prev_num_children = 1;

		//count number of children at next depth
		for (int x = 0; x < myqueue.size(); x ++)
		{
			Node temp = myqueue.get(x);

			if (temp.getLeftNode() != null)
			{
				number_of_children = number_of_children + 1;
			}
			
			if (temp.getRightNode() != null)
			{
				number_of_children = number_of_children + 1;
			}

			//System.out.println("number of children = " + number_of_children);

		}

		ArrayList<LinkedList<Node>> list_of_lists = new ArrayList<LinkedList<Node>>();

		int depth = 1;	// keep track of what depth we are in the binary tree

		LinkedList<Node> depth_list = new LinkedList<Node>();  //new list for our depth

		int counter = 0;

		while (myqueue.isEmpty() == false)
		{
			Node temp = myqueue.poll();

			depth_list.add(temp);
			System.out.println("adding node to depth list " + temp.data);

			if (counter == number_of_children && depth_list.size() == prev_num_children) //check if we've reached a new depth
			{
				counter = 0;
				prev_num_children = number_of_children;
				number_of_children = 0;

				//count number of children at next depth
				for (int x = 0; x < myqueue.size(); x ++)
				{
					Node temp2 = myqueue.get(x);

					if (temp2.getLeftNode() != null)
					{
						number_of_children = number_of_children + 1;
					}
					
					if (temp2.getRightNode() != null)
					{
						number_of_children = number_of_children + 1;
					}
				}

				list_of_lists.add(depth_list);
				//System.out.println("depth size = " + depth_list.size());

				depth = depth + 1;

				depth_list = new LinkedList<Node>();

				continue;
			}

			Node n = temp.getLeftNode();

			if (n != null)
			{
				myqueue.add(n);  //add to the queue
				counter = counter + 1;
			}

			if (counter == number_of_children && depth_list.size() == prev_num_children) //check if we've reached a new depth
			{
				counter = 0;
				prev_num_children = number_of_children;
				number_of_children = 0;

				//count number of children at next depth
				for (int x = 0; x < myqueue.size(); x ++)
				{
					Node temp2 = myqueue.get(x);

					if (temp2.getLeftNode() != null)
					{
						number_of_children = number_of_children + 1;
					}
					
					if (temp2.getRightNode() != null)
					{
						number_of_children = number_of_children + 1;
					}
				}

				list_of_lists.add(depth_list);
				//System.out.println("depth size = " + depth_list.size());

				depth = depth + 1;

				depth_list = new LinkedList<Node>();

				continue;
			}

			n = temp.getRightNode();

			if (n != null)
			{
				myqueue.add(n);  //add to the queue
				counter = counter + 1;
			}

			if (counter == number_of_children && depth_list.size() == prev_num_children) //check if we've reached a new depth
			{
				counter = 0;
				prev_num_children = number_of_children;
				number_of_children = 0;

				//count number of children at next depth
				for (int x = 0; x < myqueue.size(); x ++)
				{
					Node temp2 = myqueue.get(x);

					if (temp2.getLeftNode() != null)
					{
						number_of_children = number_of_children + 1;
					}
					
					if (temp2.getRightNode() != null)
					{
						number_of_children = number_of_children + 1;
					}
				}

				list_of_lists.add(depth_list);
				//System.out.println("depth size = " + depth_list.size());

				//System.out.println("right num of children " + number_of_children);

				depth = depth + 1;

				depth_list = new LinkedList<Node>();

				continue;
			}

		}

		System.out.printf("Tree has depth of %d  list size is %d\n", depth-1, list_of_lists.size());
		return list_of_lists;
	}


	public static void main(String[] args)
	{
		Node a = new Node(1);
		Node b = new Node(2);
		Node c = new Node(3);
		Node d = new Node(4);
		Node e = new Node(5);
		Node f = new Node(6);
		Node g = new Node(7);
		Node h = new Node(8);

		//build my binary tree
		//f.setLeftNode(g);
		//d.setLeftNode(f);
		//b.setLeftNode(d);
		//b.setRightNode(e);
		//a.setLeftNode(b);
		//a.setRightNode(c);
		d.setLeftNode(h);
		b.setLeftNode(d);
		b.setRightNode(e);
		c.setLeftNode(f);
		c.setRightNode(g);
		a.setLeftNode(b);
		a.setRightNode(c);

		ArrayList<LinkedList<Node>> newList = Node.bfsTraversal(a);

		for (int x = 0; x < newList.size(); x++)
		{
			System.out.println(newList.get(x).size());
		}

	}


}