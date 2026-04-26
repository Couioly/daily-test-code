def dijkstra(graph, start):
    """计算从start到所有其他节点的最短距离"""
    INF = float('inf')
    dis = {node: INF for node in graph}
    dis[start] = 0
    un_visited = list(graph.keys())
    
    while un_visited:
        # 找到当前距离最小的节点
        current = None
        min_dis = INF
        for node in un_visited:
            if dis[node] < min_dis:
                min_dis = dis[node]
                current = node
        
        if current is None:
            break
        
        un_visited.remove(current)
        
        # 更新相邻节点的距离
        for neighbor, weight in graph[current].items():
            if neighbor in un_visited:
                new_dis = dis[current] + weight
                if new_dis < dis[neighbor]:
                    dis[neighbor] = new_dis
    return dis

def main():
    n = int(input())
    graph = {}
    
    for _ in range(n):
        parts = input().split()
        node1, node2, weight = parts[0], parts[1], int(parts[2])
        if node1 not in graph:
            graph[node1] = {}
        if node2 not in graph:
            graph[node2] = {}
        graph[node1][node2] = weight
        graph[node2][node1] = weight
    delivery = input().split()
    start = input().strip()
    if start not in graph:
        print("没有路径连通到所有节点")
        return
    for node in delivery:
        if node not in graph:
            print("没有路径连通到所有节点")
            return
    
    # 计算所有节点对之间的最短距离
    dis_dict = {}
    for node in graph:
        dis_dict[node] = dijkstra(graph, node)
    for node in delivery:
        if dis_dict[start][node] == float('inf'):
            print("没有路径连通到所有节点")
            return
    
    # 贪心算法选择配送顺序
    current = start
    visited = []
    total_dis = 0
    remaining = delivery.copy()
    
    while remaining:
        min_dis = float('inf')
        next_node = None
        
        # 选择当前位置到剩余配送点的最短距离
        for node in remaining:
            dis = dis_dict[current][node]
            if dis < min_dis:
                min_dis = dis
                next_node = node
        
        # 如果没有可达的配送点
        if next_node is None:
            print("没有路径连通到所有节点")
            return
        
        # 更新路径和距离
        visited.append(next_node)
        total_dis += min_dis
        current = next_node
        remaining.remove(next_node)
    print(' '.join(visited))
    print(total_dis)

if __name__ == "__main__":
    main()