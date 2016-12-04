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

	//recursive function to find first common ancestor in a binary tree for two given nodes
	public static Node firstCommonAncestor(Node a, Node b, Node root)
	{
		boolean a_left = bfsTraversal(root.getLeftNode(), a);

		boolean b_left = bfsTraversal(root.getLeftNode(), b);

		if (a_left && b_left)
		{
			return firstCommonAncestor(a, b, root.getLeftNode());
		}

		boolean a_right = bfsTraversal(root.getRightNode(), a);

		boolean b_right = bfsTraversal(root.getRightNode(), b);

		if (a_right && b_right)
		{
			return firstCommonAncestor(a, b, root.getRightNode());
		}

		//base case, found first common ancestor
		if ((a_left && b_right) || (a_right && b_left))
		{
			return root;
		}

		return null; //no common ancestor
	}

	//bfs traversal of a binary tree, start at Node a and try to find Node b
	public static boolean bfsTraversal(Node a, Node b)
	{
		// java linkedlist implements Queue interface
		LinkedList<Node> myqueue = new LinkedList<Node>();
		myqueue.add(a);

		while (myqueue.isEmpty() == false)
		{
			Node temp = myqueue.poll();

			if (temp == b)
			{
				return true; //a path exists
			}

			Node n = temp.getLeftNode();

			if (n != null)
			{
				myqueue.add(n);  //add to the queue
			}

			n = temp.getRightNode();

			if (n != null)
			{
				myqueue.add(n);  //add to the queue
			}

		}
		return false;  // no path exist
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
		/*
		f.setLeftNode(g);
		d.setLeftNode(f);
		b.setLeftNode(d);
		b.setRightNode(e);
		a.setLeftNode(b);
		a.setRightNode(c);
		*/

		d.setLeftNode(h);
		b.setLeftNode(d);
		b.setRightNode(e);
		c.setLeftNode(f);
		c.setRightNode(g);
		a.setLeftNode(b);
		a.setRightNode(c);

		Node fca = Node.firstCommonAncestor(h, e, a);

		System.out.println("First common ancestor  " + fca.data);

		fca = Node.firstCommonAncestor(g, b, a);

		System.out.println("First common ancestor  " + fca.data);

		fca = Node.firstCommonAncestor(d, e, a);

		System.out.println("First common ancestor  " + fca.data);

		fca = Node.firstCommonAncestor(h, f, a);

		System.out.println("First common ancestor  " + fca.data);

		fca = Node.firstCommonAncestor(g, f, a);

		System.out.println("First common ancestor  " + fca.data);
	}
}