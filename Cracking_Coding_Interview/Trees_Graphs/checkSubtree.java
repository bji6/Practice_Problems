// ben isenberg 9/24/2016
import java.util.*;

class Node
{
	public Node left_child;
	public Node right_child;
	public String data;

	public Node(String n)
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

	//preorder traversal DFS
	public static String DFS(Node a)
	{
		if (a == null)
		{
			return "#";
		}

		String my_str = DFS(a.getLeftNode());

		my_str = my_str + a.data;

		my_str = my_str + DFS(a.getRightNode());

		return my_str;
	}

	//check if b is a subtree of a
	public static boolean checkSubtree(Node a, Node b)
	{
		String a_nodes = Node.DFS(a);
		String b_nodes = Node.DFS(b);

		return a_nodes.contains(b_nodes);
	}

	
	public static void main(String[] args)
	{
		Node a = new Node("A");
		Node b = new Node("B");
		Node c = new Node("C");
		Node d = new Node("D");
		Node e = new Node("E");
		Node f = new Node("F");
		Node g = new Node("G");
		Node h = new Node("H");

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

		System.out.println(Node.DFS(a));

		Node x = new Node("C");
		Node y = new Node("F");
		Node z = new Node("G");

		x.setLeftNode(y);
		x.setRightNode(z);

		System.out.println("B is a subtree of A ? " + Node.checkSubtree(a,x));
	}
}