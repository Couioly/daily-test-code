def create():
    n = int(input())    
    orders = []
    for i in range(n):
        id, weight, value = input().split()
        weight = int(weight)
        value = int(value)
        unit_value = value / weight 
        orders.append((id, weight, value, unit_value))    
    capacity = int(input())

    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x[3] > pivot[3]]
        middle = [x for x in arr if x[3] == pivot[3]]
        right = [x for x in arr if x[3] < pivot[3]]
        return quick_sort(left) + middle + quick_sort(right)
    
    orders = quick_sort(orders)
    return orders, capacity
  
def select(orders, capacity):
    best_orders = []
    best_value = 0
    best_count = 0
    
    for start in range(len(orders)):
        selected = []
        total_weight = 0
        total_value = 0
        
        for i in range(start, len(orders)):
            order = orders[i]
            id, weight, value, unit_value = order
            
            if total_weight + weight <= capacity:
                selected.append(id)
                total_weight += weight
                total_value += value
        
        # 更新最优方案：价值更高，或价值相同但订单数更多
        if (total_value > best_value) or (total_value == best_value and len(selected) > best_count):
            best_value = total_value
            best_count = len(selected)
            best_orders = selected
    
    # 对订单编号进行升序排序
    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)
    
    best_orders = quick_sort(best_orders)
    return best_orders, best_value

if __name__ == "__main__":
    orders, capacity = create()
    selected_orders, max_value = select(orders, capacity)
    print(" ".join(selected_orders) if selected_orders else "")
    print(max_value)