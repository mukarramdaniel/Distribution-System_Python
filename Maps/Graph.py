import math
import networkx as nx

class LocatioNode:
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
        duration = result['rows'][0]['elements'][0]['duration']['text']
        return distance
    
class Graph:
    def __init__(self) -> None:
        
        self.__graph = nx.complete_graph(0)
    def addNode(self,lati,longi):
        self.__graph.add_node(LocatioNode(lati,longi))
    def makeCompleteGraph(self):
        for i, node1 in enumerate(self.__graph.nodes):
            for j, node2 in enumerate(self.__graph.nodes):
                if i < j:
                    distance = node1.distance_to(node2)
                    self.__graph.add_edge(node1, node2, weight=distance)
    def calculateMST(self):
        self.mst = nx.minimum_spanning_tree(self.__graph, weight='weight')
    def returnMST(self):
        list=[]
        for n, data in self.mst.nodes(data=True):
            list.append((n.latitude, n.longitude))
        return list
        
        
        






# Calculate the minimum spanning tree of the graph
# Print the attributes of the nodes in the MST

# Print the edges of the MST
# total=0
# for u, v, data in mst.edges(data=True):
#     total=data['weight']+total
# print(total)

