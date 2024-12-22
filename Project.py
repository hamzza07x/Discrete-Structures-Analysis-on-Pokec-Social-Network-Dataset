import random
import heapq

from collections import defaultdict
from itertools import combinations, permutations


class User:
    def __init__(self, id_user, age, competition_level, region, status, last_login):
        self.User_ID = id_user
        self.User_age = age
        self.User_competition_percentage = competition_level
        self.User_region = region
        self.User_status = status
        self.User_last_login = last_login

    def display_user_info(self, users):
        ID = int(input("Enter user id for info: "))
        for u in users:
            if u.User_ID == ID:
                print(f"User ID: {u.User_ID}")
                print(f"User age: {u.User_age}")
                print(f"User competition percentage: {u.User_competition_percentage}%")
                print(f"User status: {u.User_status}")
                print(f"User region: {u.User_region}")
                print(f"User last login: {u.User_last_login}")
                break
        else:
            print(f"No user with ID: {ID}")

    def check_proposition(self, users):
        results = []
        prop_type = input("Enter proposition type (Age competition or Last login): ").strip()

        if prop_type.lower() == "age competition":
            results = [
                user
                for user in users
                if user.User_age > 30 and user.User_competition_percentage > 50
            ]
            print(f"Users over age 30 and competition percentage greater than 50: {len(results)}")
        elif prop_type.lower() == "last login":
            results = [
                user
                for user in users
                if user.User_last_login <= 365
            ]
            print(f"Users who logged in within the last year: {len(results)}")
        else:
            print("Invalid proposition type entered.")

        return results

    def check_Quantifiers(self, users):
        zilinsky_users = [
            user
            for user in users
            if user.User_region == "zilinsky" and user.User_age > 25 and user.User_competition_percentage > 70
        ]
        print(
            f"There exists a user in Zilinsky with age above 25 and competition percentage above 70: {bool(zilinsky_users)}"
        )
        bratislava_users = [
            user
            for user in users
            if user.User_region == "bratislava" and user.User_age > 18 and user.User_competition_percentage < 50
        ]
        print(
            f"There exists a user in Bratislava with age above 18 and competition percentage less than 50: {bool(bratislava_users)}"
        )
        return zilinsky_users and bratislava_users

    def set_operations(self, users):
        set_a = {
            user.User_ID
            for user in users
            if user.User_status == True
        }
        set_b = {
            user.User_ID
            for user in users
            if user.User_region == "bratislava"
        }
        universal_set = {
            user.User_ID
            for user in users
        }
        union_set = set_a | set_b
        intersection_sets = set_a & set_b
        complement_a = universal_set - set_a
        complement_b = universal_set - set_b
        print(f"Set A: {set_a}")
        print(f"Set B: {set_b}")
        print(f"Union: {union_set}")
        print(f"Intersection: {intersection_sets}")
        print(f"Complement of A: {complement_a}")
        print(f"Complement of B: {complement_b}")

    def function_analysis(self, users):
        user_mapping = {user.User_ID: user.User_competition_percentage for user in users}
        domain_set = set(user_mapping.keys())
        range_set = set(user_mapping.values())
        injective_check = len(user_mapping) == len(range_set)
        surjective_check = set(range(101)).issubset(range_set)
        print(f"Domain: {domain_set}")
        print(f"Range: {range_set}")
        print(f"Injective: {injective_check}")
        print(f"Surjective: {surjective_check}")

    def venn_diagram_presentation(self, users):
        public_set = {user.User_ID for user in users if user.User_status}
        age_above_30_set = {user.User_ID for user in users if user.User_age > 30}
        zilinsky_set = {user.User_ID for user in users if user.User_region == "zilinsky"}
        bratislava_set = {user.User_ID for user in users if user.User_region == "bratislava"}
        union_set = public_set | age_above_30_set | zilinsky_set | bratislava_set
        intersection_all = public_set & age_above_30_set & zilinsky_set & bratislava_set
        print(f"Public users: {len(public_set)}")
        print(f"Users above 30: {len(age_above_30_set)}")
        print(f"Union set: {len(union_set)}")
        print(f"Intersection of all sets: {len(intersection_all)}")

    def analyze_relationships(self, friendships, users):
        user_set = {user.User_ID for user in users}
        friendship_set = set(friendships)
        reflexive = all((user_id, user_id) in friendship_set for user_id in user_set)
        symmetric = all((b, a) in friendship_set for (a, b) in friendship_set)
        transitive = True
        suggestions = []
        for a, b in friendship_set:
            for c in user_set:
                if (b, c) in friendship_set and (a, c) not in friendship_set:
                    transitive = False
                    suggestions.append((a, c))
        print(f"Reflexive: {'Yes' if reflexive else 'No'}")
        print(f"Symmetric: {'Yes' if symmetric else 'No'}")
        print(f"Transitive: {'Yes' if transitive else 'No'}")
        if not transitive:
            print("Suggested friendships to make the relation transitive:")
            for a, c in suggestions:
                print(f"{a} -> {c}")

    def induction_analysis(self, users):
        threshold = int(input("Enter the threshold for competition percentage: "))
        x = int(input("Enter minimum count of users to check: "))
        count = sum(user.User_competition_percentage > threshold for user in users)
        if count > x:
            print("Induction hypothesis verified.")
        else:
            print("Induction hypothesis failed.")

    def permutations_and_combinations(self, users):
        age_filtered_users = [user for user in users if user.User_age > 25 and user.User_region == "bratislava"]
        print(f"Number of combinations: {len(list(combinations(age_filtered_users, 2)))}")
        print(f"Number of permutations: {len(list(permutations(age_filtered_users, 2)))}")

    def counting_features(self, users):
        high_completion_users = [
            user for user in users if user.User_competition_percentage > 80
        ]
        total_high_completion = len(high_completion_users)
        print(f"Total users with profile completion above 80%: {total_high_completion}")

        region_count = defaultdict(int)
        for user in users:
            region_count[user.User_region] += 1
        print("\nNumber of users in each region:")
        for region, count in region_count.items():
            print(f"{region}: {count}")

        public_profiles_count = sum(user.User_status for user in users)
        print(f"\nTotal public profiles: {public_profiles_count}")

    # Graph Class


import heapq
from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(dict)  # A dictionary of dictionaries to store weights

    def add_edge(self, u, v, weight=1):
        """Adds an edge between user u and user v with a specified weight"""
        self.graph[u][v] = weight
        self.graph[v][u] = weight  # For undirected graph

    def display_graph(self):
        """Displays the graph with edges and their weights"""
        print("Graph representation (Adjacency List with Weights):")
        for node in self.graph:
            for neighbor, weight in self.graph[node].items():
                print(f"User {node} is connected to User {neighbor} with weight {weight}")

    def minimum_spanning_tree(self):
        """Finds the minimum spanning tree using Prim's algorithm"""
        if not self.graph:
            print("Graph is empty. No MST can be found.")
            return

        start_node = next(iter(self.graph))  # Start from any node in the graph
        visited = set()  # Track visited nodes
        min_heap = [(0, start_node)]  # (weight, node)
        mst_edges = []  # To store MST edges

        while min_heap:
            weight, node = heapq.heappop(min_heap)  # Pop the node with the smallest edge weight

            if node not in visited:
                visited.add(node)
                if weight > 0:  # If weight is > 0, add edge to MST edges
                    mst_edges.append((weight, node))

                # Explore neighbors (edges) of the current node
                for neighbor, edge_weight in self.graph[node].items():
                    if neighbor not in visited:
                        heapq.heappush(min_heap, (edge_weight, neighbor))

        # Print the MST edges
        print("Minimum Spanning Tree (MST) edges:")
        for weight, node in mst_edges:
            print(f"Node: {node}, Weight: {weight}")

    def is_bipartite(self):
        """Check if the graph is bipartite"""
        color = {}  # To store colors of the nodes
        for start_node in self.graph:
            if start_node not in color:
                # Perform BFS to check for bipartiteness
                queue = deque([start_node])
                color[start_node] = 0  # Start coloring with 0 (one color)
                while queue:
                    node = queue.popleft()
                    current_color = color[node]
                    for neighbor in self.graph[node]:
                        if neighbor not in color:
                            # Color the neighbor with opposite color
                            color[neighbor] = 1 - current_color
                            queue.append(neighbor)
                        elif color[neighbor] == current_color:
                            # If a neighbor has the same color, it's not bipartite
                            print("Graph is not bipartite.")
                            return False
        print("Graph is bipartite.")
        return True

    def bfs(self, start):
        """Breadth-First Search (BFS) starting from node 'start'"""
        visited = set()
        queue = deque([start])
        bfs_order = []

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                bfs_order.append(node)
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)

        print("BFS traversal order:", bfs_order)
        return bfs_order

    def dfs(self, start):
        """Depth-First Search (DFS) starting from node 'start'"""
        visited = set()
        dfs_order = []

        def dfs_recursive(node):
            visited.add(node)
            dfs_order.append(node)
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    dfs_recursive(neighbor)

        dfs_recursive(start)
        print("DFS traversal order:", dfs_order)
        return dfs_order

    def connected_components(self):
        """Finds the connected components in the graph using DFS"""
        visited = set()
        components = []

        def dfs(node, component):
            visited.add(node)
            component.append(node)
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, component)

        for node in self.graph:
            if node not in visited:
                component = []
                dfs(node, component)
                components.append(component)

        return components

    def are_friends(self, user1, user2):
        """Checks if two users are friends (directly connected)"""
        return user2 in self.graph.get(user1, [])

    def add_node(self, node):
        """Adds a node to the graph (with no edges)"""
        if node not in self.graph:
            self.graph[node] = {}




# Tree Class
class TreeNode:
    def __init__(self, user_id):
        self.user_id = user_id
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)


class Tree:
    def __init__(self):
        self.root = None
        self.nodes = {}  # To keep track of user_id to TreeNode mapping

    def add_node(self, user_id, parent_id=None):
        """Add a node (user) to the tree"""
        new_node = TreeNode(user_id)
        self.nodes[user_id] = new_node
        if parent_id is None:
            # Root node (first user added is the root)
            if self.root is None:
                self.root = new_node
        else:
            parent_node = self.nodes.get(parent_id)
            if parent_node:
                parent_node.add_child(new_node)

    def display_tree(self, node=None, level=0):
        """Display the tree structure"""
        if node is None:
            node = self.root
        print("  " * level + f"User {node.user_id}")
        for child in node.children:
            self.display_tree(child, level + 1)


def generate_users_and_friendships(file_path_profiles, file_path_relationships, user_lines, friendship_lines):
    users = []
    friendships = []
    graph = Graph()  # Create a Graph object
    tree = Tree()  # Create a Tree object
    regions = ['zilinsky', 'bratislava']

    try:
        with open(file_path_profiles, 'r', encoding='utf-8') as file:
            for i, line in enumerate(file):
                if user_lines is not None and i >= user_lines:
                    break
                data = line.strip().split('\t')

                # Debugging print
                print(f"Processing line {i}: {data}")

                if len(data) < 6:  # Ensure there are at least 6 elements
                    print(f"Warning: Incomplete data at line {i}, skipping.")
                    continue  # Skip this line if there aren't enough columns

                try:
                    user_id = int(data[0])  # User ID
                    age = int(data[2]) if data[2].isdigit() else random.randint(16,
                                                                                60)  # Age (default random if invalid)

                    # Now competition_level will be extracted safely from data[5], if available
                    competition_level = int(data[5]) if len(data) > 5 and data[5].isdigit() else random.randint(0,
                                                                                                                100)  # Default to random if missing or invalid

                    region = next((region for region in regions if region in data[3].lower()),
                                  'unknown')  # Region (defaults to 'unknown' if not found)
                    status = bool(int(data[4]))  # Status (boolean)
                    last_login = random.randint(0, 365)  # Random last login time

                    # Add user object to the users list
                    users.append(User(user_id, age, competition_level, region, status, last_login))
                    tree.add_node(user_id)  # Add each user to the tree

                except (IndexError, ValueError) as e:
                    # If any parsing error occurs (e.g., missing data, conversion failure), print the error and skip the line
                    print(f"Error processing line {i}: {e}")
                    continue
    except FileNotFoundError:
        print(f"Error: File '{file_path_profiles}' not found.")

    # Now handle the friendships part similarly:
    try:
        with open(file_path_relationships, 'r', encoding='utf-8') as file:
            for i, line in enumerate(file):
                if friendship_lines is not None and i >= friendship_lines:
                    break
                try:
                    user1, user2 = map(int,
                                       line.strip().split('\t'))  # Extract user1 and user2 from the friendship line
                    friendships.append((user1, user2))
                    graph.add_edge(user1, user2)  # Add friendship edge to the graph
                    # Here, you can assign parent-child relationships in the tree
                    if random.random() < 0.5:  # Randomly assign a parent-child relationship
                        parent_id = user1
                        tree.add_node(user2, parent_id)  # Add user2 as a child of user1
                except ValueError:
                    # If parsing the friendship fails (invalid data format), skip this line
                    continue
    except FileNotFoundError:
        print(f"Error: File '{file_path_relationships}' not found.")

    # Return the users, friendships, graph, and tree objects
    return users, friendships, graph, tree


def welcome_interface():
    print("*")
    print("*   Welcome to Enhanced Discrete Structures Project.  *")
    print("*")


def main():
    welcome_interface()
    file_path_profiles = "soc-pokec-profiles.txt"
    file_path_relationships = "soc-pokec-relationships.txt"

    # Get number of lines to process
    user_lines = int(input("Enter number of lines to compute from profiles document: "))
    print("\n")
    friendship_lines = int(input("Enter number of lines to compute from relationships document: "))

    # Generate users and friendships (build the graph)
    users, friendships, graph, tree = generate_users_and_friendships(file_path_profiles, file_path_relationships,
                                                                     user_lines, friendship_lines)

    # Ensure the graph is populated
    if not graph:
        print("Graph is empty. Please check input data.")
        return

    user = users[0]  # Example user for displaying info
    print("1. Display/edit")
    print("2. Check proposition")
    print("3. Check Quantifiers")
    print("4. Set operations")
    print("5. Function analysis")
    print("6. Venn diagram")
    print("7. Relations analysis")
    print("8. Induction analysis")
    print("9. Permutation and combination")
    print("10. Counting")
    print("11. Display graph")
    print("12. Connected components")
    print("13. Are two users friends?")
    print("14. Display tree")
    print("15. Minimum Spanning Tree (MST)")
    print("16. Check if Graph is Bipartite")
    print("17. Depth-First Search (DFS)")
    print("18. Breadth-First Search (BFS)")
    print("19. Exit")

    while True:
        user_choice = int(input("Enter Discrete structures to compute: "))

        # Call the corresponding functions based on user input
        if user_choice == 1:
            user.display_user_info(users)
        elif user_choice == 2:
            user.check_proposition(users)
        elif user_choice == 3:
            user.check_Quantifiers(users)
        elif user_choice == 4:
            user.set_operations(users)
        elif user_choice == 5:
            user.function_analysis(users)
        elif user_choice == 6:
            user.venn_diagram_presentation(users)
        elif user_choice == 7:
            user.analyze_relationships(friendships, users)
        elif user_choice == 8:
            user.induction_analysis(users)
        elif user_choice == 9:
            user.permutations_and_combinations(users)
        elif user_choice == 10:
            user.counting_features(users)
        elif user_choice == 11:
            graph.display_graph()  # Display the graph
        elif user_choice == 12:
            components = graph.connected_components()  # Get connected components
            print("Connected components:")
            for component in components:
                print(component)
        elif user_choice == 13:
            user1 = int(input("Enter the first user ID: "))
            user2 = int(input("Enter the second user ID:4 "))
            if graph.are_friends(user1, user2):
                print(f"User {user1} and User {user2} are friends.")
            else:
                print(f"User {user1} and User {user2} are not friends.")
        elif user_choice == 14:
            tree.display_tree()  # Display the tree structure
        elif user_choice == 15:
            graph.minimum_spanning_tree()  # Call MST after graph is generated
        elif user_choice == 16:
            if graph.is_bipartite():
                print("The graph is bipartite.")
            else:
                print("The graph is not bipartite.")
        elif user_choice == 17:
            start_node = int(input("Enter starting node for DFS: "))
            print("DFS traversal starting from node", start_node)
            graph.dfs(start_node)
        elif user_choice == 18:
            start_node = int(input("Enter starting node for BFS: "))
            print("BFS traversal starting from node", start_node)
            graph.bfs(start_node)
        elif user_choice == 19:
            print("Exiting...")
            break  # Exit the program
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()