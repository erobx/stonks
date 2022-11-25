"""

RUN THIS FILE TO GENERATE HTML FILE OF THE VISUALIZER

"""
from pyvis.network import Network

def main():

    # creates graph with settings
    # net = Network(height= "110vh", bgcolor="#1c77ac")
    net = Network(height= "110vh")
    net.toggle_physics(True)

    # testing adding nodes and edges
    net.add_node(1, label="APPL", shape="image", image="https://www.apple.com/ac/structured-data/images/knowledge_graph_logo.png?202110180743") # node id = 1 and label = Node 1
    net.add_node(2, label="MSFT", shape="image", image="https://eodhistoricaldata.com//img/logos/US/MSFT.png") # node id and label = 2
    net.add_node(3)
    net.add_node(4)

    net.add_edge(1, 2, weight=10) # edge from 1 to 2 with weight 10
    net.add_edge(1, 3, weight=20)
    net.add_edge(1, 4, weight=500)


    # generates html file of graph visualizer to respective directory
    net.generate_html('./templates/mygraph.html')
    net.write_html('./templates/mygraph.html')


if __name__ == "__main__":
    main()





