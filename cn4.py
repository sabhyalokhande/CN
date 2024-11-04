class Router:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.distance_matrix = [[float('inf')] * num_nodes for _ in range(num_nodes)]
        self.next_hop = [[-1] * num_nodes for _ in range(num_nodes)]
        self.initialize_router()

    def initialize_router(self):
        # Initialize the distance matrix and next hop matrix
        for i in range(self.num_nodes):
            self.distance_matrix[i][i] = 0
            self.next_hop[i][i] = i

    def set_edge(self, src, dest, cost):
        self.distance_matrix[src][dest] = cost
        self.distance_matrix[dest][src] = cost
        self.next_hop[src][dest] = dest
        self.next_hop[dest][src] = src

    def update_routing_table(self):
        for k in range(self.num_nodes):
            for i in range(self.num_nodes):
                for j in range(self.num_nodes):
                    if self.distance_matrix[i][k] + self.distance_matrix[k][j] < self.distance_matrix[i][j]:
                        self.distance_matrix[i][j] = self.distance_matrix[i][k] + self.distance_matrix[k][j]
                        self.next_hop[i][j] = self.next_hop[i][k]

    def print_routing_table(self):
        print("\nDistance Vector Routing Table:")
        for i in range(self.num_nodes):
            print(f"Router {i + 1}:")
            for j in range(self.num_nodes):
                print(f"  To {j + 1}: Cost = {self.distance_matrix[i][j]}, Next hop = {self.next_hop[i][j] + 1}")
            print()

# Get user input
def get_user_input():
    num_nodes = int(input("Enter the number of routers: "))
    router = Router(num_nodes)

    print("\nEnter the cost of the links (enter -1 if no direct link exists):")
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            cost = int(input(f"Cost between Router {i + 1} and Router {j + 1}: "))
            if cost != -1:
                router.set_edge(i, j, cost)

    return router

# Main program
if __name__ == "__main__":
    router = get_user_input()
    print("\nUpdating routing tables using Distance Vector Routing Protocol...")
    router.update_routing_table()
    router.print_routing_table()

