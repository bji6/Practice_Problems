// ben isenberg 9/25/2016
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

	//inorder traversal DFS, summing nodes to find path to value
	public static void DFS(Node a, int sum, int value)
	{
		if (a == null)
		{
			return;
		}

		sum = sum + a.data;
		//System.out.println(a.data);

		if (sum == value)
		{
			System.out.println("We found a path to " + value);
		}

		DFS(a.getLeftNode(),sum,value);

		DFS(a.getRightNode(),sum,value);

		return;
	}

	//bfs traversal of a binary tree, run DFS at each node to find all possible sum paths from each node
	public static void bfsTraversal(Node a, int value)
	{
		// java linkedlist implements Queue interface
		LinkedList<Node> myqueue = new LinkedList<Node>();
		myqueue.add(a);

		while (myqueue.isEmpty() == false)
		{
			Node temp = myqueue.poll();

			Node.DFS(temp, 0, value);		// find all sum paths starting from this Node

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
		return;
	}

	
	public static void main(String[] args)
	{
		Node a = new Node(3);
		Node b = new Node(4);
		Node c = new Node(6);
		Node d = new Node(-2);
		Node e = new Node(1);
		Node f = new Node(2);
		Node g = new Node(-3);
		Node h = new Node(4);
		Node i = new Node(2);
		Node j = new Node(10);
		Node k = new Node(-3);

		//build my binary tree
		d.setLeftNode(e);
		d.setRightNode(f);
		g.setLeftNode(h);
		g.setRightNode(i);
		j.setLeftNode(k);
		b.setLeftNode(d);
		c.setLeftNode(g);
		c.setRightNode(j);
		a.setLeftNode(b);
		a.setRightNode(c);

		Node.bfsTraversal(a,7);
		Node.bfsTraversal(a,3);
	}
}