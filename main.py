def longest_path(graph: list) -> int:
    def topological_sort(graph):
        in_degree = [0] * len(graph)
        for u in range(len(graph)):
            for v, w in graph[u]:
                in_degree[v] += 1

        queue = [u for u in range(len(graph)) if in_degree[u] == 0]
        topo_order = []

        while queue:
            u = queue.pop(0)
            topo_order.append(u)
            for v, w in graph[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

        return topo_order

    def calculate_longest_path(graph, topo_order):
        dp = [-float('inf')] * len(graph)
        dp[0] = 0

        for u in topo_order:
            if dp[u] != -float('inf'):
                for v, w in graph[u]:
                    if dp[v] < dp[u] + w:
                        dp[v] = dp[u] + w

        return max(dp)

    topo_order = topological_sort(graph)
    return calculate_longest_path(graph, topo_order)

if __name__ == "__main__":
    graph = eval(input().strip())
    print(longest_path(graph))
