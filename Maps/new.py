import math
import networkx as nx

class LocationNode:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        

    def distance_to(self, other):
        
        R = 6371 
        lati = math.radians(other.latitude-self.latitude)
        longi = math.radians(other.longitude-self.longitude)
        a = math.sin(lati/2) * math.sin(lati/2) + math.cos(math.radians(self.latitude)) * math.cos(math.radians(other.latitude)) * math.sin(longi/2) * math.sin(longi/2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        d = R * c 
        return d
        # import googlemaps
        # gmaps = googlemaps.Client('AIzaSyBebwTrA8E0hXbyw8R2dUQRTFOg7q517U0')
        # origin = (self.latitude, other.longitude)
        # destination = (self.longitude, other.longitude)
        # result = gmaps.distance_matrix(origin, destination)
        # distance = result['rows'][0]['elements'][0]['distance']['text']
        # duration = result['rows'][0]['elements'][0]['duration']['text']
        # return distance

# Create a complete graph with four nodes
G = nx.complete_graph(0)

# Add the nodes to the graph
node1 = LocationNode(31.57714030411648, 74.35603665613657)
node3 = LocationNode(31.55043477797966, 74.31304116179827)
node4 = LocationNode(31.57552403504949, 74.35429530639927)
node2 = LocationNode(31.577244438074196, 74.358372424896)

G.add_node(node1)
G.add_node(node2)
G.add_node(node3)
G.add_node(node4)

# Add the edges to the graph with the calculated distances as weights
l=list(G.nodes)
for i, node1 in enumerate(G.nodes):
    for j, node2 in enumerate(G.nodes):
        if i < j:
            distance = node1.distance_to(node2)
            G.add_edge(node1, node2, weight=distance)

# Calculate the minimum spanning tree of the graph
mst = nx.minimum_spanning_tree(G, weight='weight')
# Print the attributes of the nodes in the MST
for n, data in mst.nodes(data=True):
    print(f"{n}: {n.latitude}, {n.longitude}")
# Print the edges of the MST
total=0
for u, v, data in mst.edges(data=True):
    total=data['weight']+total
print(total)

