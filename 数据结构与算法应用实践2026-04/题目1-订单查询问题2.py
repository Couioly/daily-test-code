def create_orders():
    n = int(input())
    orders_id = {}
    orders_address = {}
    
    for i in range(n):
        id, address, weight = input().split(",")
        weight = float(weight)
        orders_id[id] = (address, weight)
        
        if address not in orders_address:
            orders_address[address] = {
                'ids': [],
                'total_weight': 0.0
            }
        
        ids = orders_address[address]['ids']

        inserted = False
        for i in range(len(ids)):
            if id < ids[i]:
                ids.insert(i, id)
                inserted = True
                break
        if not inserted:
            ids.append(id)

        orders_address[address]['total_weight'] += weight
    return orders_id, orders_address

def query(orders_id, orders_address):
    k = int(input())
    results = []

    for i in range(k):
        type_str, data = input().split(" ")
        if type_str == "1":
            results.append(query1(data, orders_id))
        elif type_str == "2":
            results.append(query2(data, orders_address))
    return results

def query1(data, orders_id):
    if data in orders_id:
        return orders_id[data][0]
    return "没有此订单"

def query2(data, orders_address):
    if data not in orders_address:
        return "订单中没有要配送到此地点的订单"
    
    orders_info = orders_address[data]
    ids = orders_info['ids']
    weight = orders_info['total_weight']
    
    result = " ".join(ids)
    return f"{result} {weight:.1f}"

if __name__ == "__main__":
    orders_id, orders_address = create_orders()
    for result in query(orders_id, orders_address):
        print(result)