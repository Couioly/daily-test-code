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

    # 快速排序按单位价值降序排序
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
    selected_orders = [] 
    total_weight = 0       
    total_value = 0
    
    for order in orders:
        id, weight, value, unit_value = order
        
        if total_weight + weight <= capacity:
            selected_orders.append(id)
            total_weight += weight
            total_value += value
    
    # 对订单编号进行升序排序
    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)
    
    selected_orders = quick_sort(selected_orders)
    return selected_orders, total_value

if __name__ == "__main__":
    orders, capacity = create()
    selected_orders, max_value = select(orders, capacity)
    print(" ".join(selected_orders) if selected_orders else "")
    print(max_value)