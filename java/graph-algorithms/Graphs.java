/*
 * Java code to demonstrate basic graph algorithms. Closely Follows the algorithms and notations used in
 * "Introduction to Algorithms" by Cormen, Leiserson, Rivest, Stein. 
 * 
 * Author: Sahand Saba
 * 
 */
import java.util.Comparator;
import java.util.LinkedList;
import java.util.PriorityQueue;

public class Graphs {
	public static void outputShortestPathTestResults(String algorithm, Graph g,
			Vertex s, Vertex t, int returnedValue) {
		System.out.println(algorithm + " - Shortest path from " + s.getLabel()
				+ " to " + t.getLabel());
		System.out.println(returnedValue);
		if (returnedValue == -1) {
			System.out.println("Found negative cycle! No shortest path.");
			return;
		}
		LinkedList<Vertex> path = new LinkedList<Vertex>();
		g.getShortestPath(t, path);
		for (Vertex v : path) {
			System.out.print(v.getLabel());
		}
		System.out.println("\n");
	}

	public static void main(String[] args) {
		Graph g = new Graph();
		Vertex s, t, x, y, z;
		s = g.addVertex("s");
		t = g.addVertex("t");
		x = g.addVertex("x");
		y = g.addVertex("y");
		z = g.addVertex("z");

		// This graph is the one on page 648 of CLRS, Third Edition
		Edge st = s.addEdge(3, t);
		Edge sy = s.addEdge(5, y);
		Edge tx = t.addEdge(6, x);
		Edge ty = t.addEdge(2, y);
		Edge xz = x.addEdge(2, z);
		Edge yz = y.addEdge(6, z);
		Edge yx = y.addEdge(4, x);
		Edge yt = y.addEdge(1, t);
		Edge zx = z.addEdge(7, x);
		Edge zs = z.addEdge(3, s);

		int r = g.bfs(s, z);
		outputShortestPathTestResults("BFS", g, s, z, r);

		r = g.bellmanFord(s, z);
		outputShortestPathTestResults("Bellman-Ford", g, s, z, r);

		r = g.dijkstra(s, z);
		outputShortestPathTestResults("Dijkstra's", g, s, z, r);

		// Let's introduce a negative cycle s->y->z->s
		sy.setWeight(-1);
		yz.setWeight(-1);
		zs.setWeight(-1);

		r = g.bellmanFord(s, z);
		outputShortestPathTestResults("Bellman-Ford", g, s, z, r);
	}
}

class Graph {
	private LinkedList<Vertex> vertices;

	public LinkedList<Vertex> getVertices() {
		return vertices;
	}

	public LinkedList<Edge> getEdges() {
		return edges;
	}

	private LinkedList<Edge> edges;

	public Graph() {
		super();
		this.vertices = new LinkedList<Vertex>();
		this.edges = new LinkedList<Edge>();
	}

	public Vertex addVertex(String label) {
		Vertex v = new Vertex(this, label);
		this.vertices.add(v);
		return v;
	}

	@Override
	public String toString() {
		java.lang.StringBuilder sb = new StringBuilder();
		for (Vertex v : this.vertices) {
			sb.append(v.getLabel());
			sb.append(": ");
			for (Edge e : v.getEdges()) {
				sb.append(e.getTarget().getLabel());
				sb.append(' ');
				sb.append(e.getWeight());
				sb.append(' ');
			}
			sb.append("\n");
		}
		return sb.toString();
	}

	// Returns shortest path to t from s without considering weights (i.e. all
	// edges have the same weight).
	// Returns Integer.MAX_VALUE if t is not reachable from s.
	// The shortest path can be retrieved using getShortestPath after a call to
	// this method.
	public int bfs(Vertex s, Vertex t) {
		this.initializeSingleSource(s);
		LinkedList<Vertex> Q = new LinkedList<Vertex>();
		Q.addFirst(s);
		while (Q.size() > 0) {
			Vertex v = Q.removeLast();
			for (Edge e : v.getEdges()) {
				Vertex u = e.getTarget();
				if (u.getColor() != VertexColor.WHITE) {
					continue;
				}
				Q.addFirst(u);
				u.setColor(VertexColor.GRAY);
				u.setShortestPathDistanceUpperBound(v
						.getShortestPathDistanceUpperBound() + 1);
				u.setPreviousVertexInShortestPath(v);
			}
			v.setColor(VertexColor.BLACK);
		}
		return t.getShortestPathDistanceUpperBound();
	}

	// To be called before single-source shortest path algorithms such as
	// Bellman-Ford or Dijkstra's are run.
	public void initializeSingleSource(Vertex s) {
		for (Vertex v : this.vertices) {
			v.setShortestPathDistanceUpperBound(Integer.MAX_VALUE);
			v.setPreviousVertexInShortestPath(null);
			v.setColor(VertexColor.WHITE);
		}
		s.setShortestPathDistanceUpperBound(0);
		s.setColor(VertexColor.GRAY);
	}

	// If the path going through e is shorter than one not going through it,
	// update the path so it goes through e and also update the upper bound on
	// the distance to e's target.
	// Returns true if the edge e was used. False otherwise.
	public boolean relaxEdge(Edge e) {
		// e is an edge from u to v with weight w
		Vertex u = e.getSource();
		Vertex v = e.getTarget();
		int w = e.getWeight();

		int distanceWithoutE = v.getShortestPathDistanceUpperBound();
		int distanceWithE = u.getShortestPathDistanceUpperBound() + w;

		if (distanceWithE < distanceWithoutE) {
			v.setShortestPathDistanceUpperBound(distanceWithE);
			v.setPreviousVertexInShortestPath(u);
			return true;
		}
		return false;
	}

	// Single-source shortest path algorithm with O(|V|*|E|) running time.
	// Returns -1 if a negative weight cycle exists.
	// Returns the weight of the shortest path otherwise.
	// The shortest path can be retrieved using getShortestPath after a call to
	// this method.
	public int bellmanFord(Vertex s, Vertex t) {
		int n = this.vertices.size();
		this.initializeSingleSource(s);
		for (int i = 0; i < n; i++) {
			for (Edge e : this.edges) {
				boolean changed = this.relaxEdge(e);
				if (changed && i == n - 1) {
					return -1;
				}
			}
		}
		return t.getShortestPathDistanceUpperBound();
	}

	// Shortest path algorithm with O(|V|*log(|V|)) running time, n = |V|
	// Returns the weight of the shortest path.
	// Does not produce the correct result if graph has negative weights.
	// The shortest path can be retrieved using getShortestPath after a call to
	// this method.
	public int dijkstra(Vertex s, Vertex t) {
		this.initializeSingleSource(s);
		Comparator<Vertex> c = new Comparator<Vertex>() {
			public int compare(Vertex v, Vertex u) {
				return v.getShortestPathDistanceUpperBound()
						- u.getShortestPathDistanceUpperBound();
			}
		};
		PriorityQueue<Vertex> Q = new PriorityQueue<Vertex>(
				this.vertices.size(), c);
		Q.add(s);
		while (Q.size() > 0) {
			Vertex v = Q.poll();
			if (v.getColor() == VertexColor.BLACK) {
				continue;
			}
			v.setColor(VertexColor.BLACK);
			for (Edge e : v.getEdges()) {
				this.relaxEdge(e);
				Q.add(e.getTarget());
			}
		}
		return t.getShortestPathDistanceUpperBound();
	}

	// To be called after a single-source shortest path algorithm is run to get
	// the shortest path
	// from the source to the given vertex t.
	public void getShortestPath(Vertex t, LinkedList<Vertex> path) {
		if (t == null) {
			return;
		}
		this.getShortestPath(t.getPreviousVertexInShortestPath(), path);
		path.add(t);
	}
}

class Edge {
	private int weight;
	private Vertex source;
	private Vertex target;

	public Edge(int weight, Vertex source, Vertex target) {
		this.weight = weight;
		this.source = source;
		this.target = target;
	}

	public int getWeight() {
		return weight;
	}

	public void setWeight(int weight) {
		this.weight = weight;
	}

	public Vertex getSource() {
		return source;
	}

	public void setSource(Vertex source) {
		this.source = source;
	}

	public Vertex getTarget() {
		return target;
	}

	public void setTarget(Vertex target) {
		this.target = target;
	}

}

enum VertexColor {
	WHITE, // Unprocessed
	GRAY, // Processing...
	BLACK // Processed
}

class Vertex {
	private Graph graph;
	private String label;
	private LinkedList<Edge> edges;

	// Previous vertex, used in shortest path algorithms
	private Vertex previousVertexInShortestPath;
	// Upper bound on the cost to get this vertex from a source
	// vertex. Used by shortest path algorithms.
	private int shortestPathDistanceUpperBound;
	// Vertex color is used to keep track of the status of a vertex in a
	// shortest path algorithm.
	private VertexColor color;

	public Vertex(Graph g, String label) {
		this.label = label;
		this.graph = g;
		this.edges = new LinkedList<Edge>();
	}

	public Vertex(Graph g, String label, LinkedList<Edge> edges) {
		super();
		this.label = label;
		this.graph = g;
		this.edges = edges;
	}

	public Edge addEdge(int weight, Vertex target) {
		Edge e = new Edge(weight, this, target);
		this.graph.getEdges().add(e);
		this.edges.add(e);
		return e;
	}

	public String getLabel() {
		return label;
	}

	public void setLabel(String label) {
		this.label = label;
	}

	public LinkedList<Edge> getEdges() {
		return edges;
	}

	public void setEdges(LinkedList<Edge> edges) {
		this.edges = edges;
	}

	public Graph getGraph() {
		return graph;
	}

	public void setGraph(Graph graph) {
		this.graph = graph;
	}

	public Vertex getPreviousVertexInShortestPath() {
		return previousVertexInShortestPath;
	}

	public void setPreviousVertexInShortestPath(Vertex pi) {
		this.previousVertexInShortestPath = pi;
	}

	public int getShortestPathDistanceUpperBound() {
		return shortestPathDistanceUpperBound;
	}

	public void setShortestPathDistanceUpperBound(int d) {
		this.shortestPathDistanceUpperBound = d;
	}

	public VertexColor getColor() {
		return color;
	}

	public void setColor(VertexColor color) {
		this.color = color;
	}
}
