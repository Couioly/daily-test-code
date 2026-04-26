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
    
    # 贪心算法选择配送顺序
    current = start
    visited = []
    total_distance = 0
    un_delivery = delivery.copy()
    
    while un_delivery:
        min_distance = float('inf')
        next_node = None
        
        # 选择当前位置到剩余配送点的最短距离
        for node in un_delivery:
            if node in graph[current]:
                distance = graph[current][node]
                if distance < min_distance:
                    min_distance = distance
                    next_node = node
        
        # 如果没有可达的配送点
        if next_node is None:
            print("没有路径连通到所有节点")
            return
        
        # 更新路径和距离
        visited.append(next_node)
        total_distance += min_distance
        current = next_node
        un_delivery.remove(next_node)

    print(' '.join(visited))
    print(total_distance)

if __name__ == "__main__":
    main()