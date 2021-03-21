def solution(bridge_length, weight, truck_weights):
    answer = 0
    weight_sum = 0
    truck_not_passed = truck_weights[::-1].copy()
    truck_on_bridge = []
    while True: 
        temp = truck_not_passed[-1]
        truck_not_passed.pop()
        truck_on_bridge.append(temp)
        weight_sum += sum(truck_on_bridge)
        if weight_sum <= weight : 
            answer += 1
        else : 
            weight_sum -= truck_on_bridge[-1]
            truck_on_bridge.pop()
            answer += (bridge_length - len(truck_on_bridge)+1)
            temp_val = truck_on_bridge[0]
            truck_on_bridge = truck_on_bridge[1:]
            weight_sum -= temp_val
        if truck_not_passed == [] : 
            answer += bridge_length
            break
    return answer