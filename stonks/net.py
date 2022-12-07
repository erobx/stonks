from pyvis.network import Network
import sys
sys.path.append('../p3')
import os.path
import query
import urllib3
import http

# 1. logo, 2. ticker, 3. pe, 4. volume, 5. price, 6. market_cap, 7. eps, 8. sector, 9. employees, 10. revenue, 11. growth, 12. profit

# for i,a in enumerate(above):
#     print(above[len(above)- i - 1])


class Node():
    def __init__(self, info):
        if (info[0] == 'none'):
            self.logo = 'static/images/stonks.jpeg'
        else:
            http = urllib3.PoolManager()
            error = http.request('GET', info[0])
            print(error.status)
            if (error.status == 404):
                self.logo = 'static/images/stonks.jpeg'
            else:
                self.logo = info[0]
        self.ticker = info[1]
        self.pe = info[2]
        self.volume = info[3]
        self.price = info[4]
        self.market_cap = info[5]
        self.eps = info[6]
        self.sector = info[7]
        self.employees = info[8]
        self.revenue = info[9]
        self.growth = info[10]
        self.profit = info[11]

template_path = os.path.abspath('stonks/templates')
write_path = os.path.join(template_path, 'mygraph.html')

def init_network():
    srcData, above, below = query.get_node_data('stonks.db', 'SMP', 'volume')
    aboveNodeList = []
    belowNodeList = []
    net = Network(height="100vh")
    net.toggle_physics(True)

    #source node
    src = Node(srcData)
    print("SRC:", src.ticker)
    n = net.add_node(src.ticker, label=src.ticker, shape="image", image=src.logo)
    aboveNodeList.append(src.ticker)
    belowNodeList.append(src.ticker)

    for i in range(len(above)):
        newNode = Node(above[len(above)- i - 1])
        aboveNodeList.append(newNode.ticker)
        net.add_node(newNode.ticker, label=newNode.ticker, shape="image", image=newNode.logo)
        net.add_edge(aboveNodeList[i], aboveNodeList[i+1])
        print("ADDED EDGE FROM", aboveNodeList[i], "--->", aboveNodeList[i+1])


    ####### TO FIX ##############
    # for i in range(len(below)):
    #     newNode = Node(above[len(above)- i - 1])
    #     aboveNodeList.append(newNode.ticker)
    #     net.add_node(newNode.ticker, label=newNode.ticker, shape="image", image=newNode.logo)
    #     net.add_edge(aboveNodeList[i], aboveNodeList[i+1])
    #     print("ADDED EDGE FROM", aboveNodeList[i], "--->", aboveNodeList[i+1])


    #net.generate_html(write_path)
    try:
        net.write_html(write_path)
    except (OSError, FileNotFoundError):
        print('')
    #net.set_template_dir(template_path, 'mygraph.html')


#init_network()

