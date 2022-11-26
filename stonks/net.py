from pyvis.network import Network
import os.path

def init_network():
    net = Network(height="100vh")
    net.toggle_physics(True)

    # testing adding nodes and edges
    net.add_node(1, label="APPL", shape="image", image="https://www.apple.com/ac/structured-data/images/knowledge_graph_logo.png?202110180743") # node id = 1 and label = Node 1
    net.add_node(2, label="MSFT", shape="image", image="https://eodhistoricaldata.com//img/logos/US/MSFT.png") # node id and label = 2
    net.add_node(3)
    net.add_node(4)

    net.add_edge(1, 2, weight=10) # edge from 1 to 2 with weight 10
    net.add_edge(1, 3, weight=20)
    net.add_edge(1, 4, weight=500)

    template_path = os.path.abspath('stonks/templates')
    write_path = os.path.join(template_path, 'mygraph.html')
    net.generate_html(write_path)

