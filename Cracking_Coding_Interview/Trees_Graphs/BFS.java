// ben isenberg 9/18/2016
import java.util.*;

class Node
{
	public Node[] adj;
	public String name;
	public int node_count;

	public Node(String n)
	{
		adj = new Node[3];
		name = n;
		node_count = 0;
	}

	public void addNode(Node x)
	{
		if (node_count > 3)
		{
			System.out.println("Node list is full");
			return;
		}

		adj[node_count] = x;
		node_count = node_count + 1;
	}

	public Node getNode(int x)
	{
		if (x > node_count)
		{
			System.out.println("Node does not exist");
			return null;
		}

		return adj[x-1];
	}

	// BFS implementation to find if path exists between 2
	// nodes in a directed graph
	public static boolean findNode(Node a, Node b)
	{
		// java linkedlist implements Queue interface
		LinkedList<Node> myqueue = new LinkedList<Node>();
		// keep track of nodes we've visited.  each node has unique name
		Hashtable<String, Boolean> marked_nodes = new Hashtable<String, Boolean>();

		marked_nodes.put(a.name, true);

		myqueue.add(a);

		while (myqueue.isEmpty() == false)
		{
			Node temp = myqueue.poll();
			marked_nodes.put(temp.name, true);  //visited a node

			if (temp == b)  //is this the node we are looking for?
			{
				System.out.printf("A path does exist from %s to %s\n", a.name, b.name);
				return true;
			}

			for (int i = 0; i < temp.node_count; i++)  //check adj list for new nodes to visit
			{
				Node n = temp.adj[i];

				if (marked_nodes.containsKey(n.name) == false) //check if alrdy visited
				{
					marked_nodes.put(n.name, true);
					myqueue.add(n);  //add to the queue
				}
			}
		}

		System.out.printf("No path does exist from %s to %s\n", a.name, b.name);
		return false;
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

		//build my directed graph
		f.addNode(g);
		d.addNode(e);
		d.addNode(a);
		c.addNode(d);
		b.addNode(b);
		a.addNode(b);
		a.addNode(f);

		Node.findNode(a, g);
		Node.findNode(c, g);
		Node.findNode(f, d);
	}
}