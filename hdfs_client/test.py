
from snakebite.client import Client

# ============================================================
def test():
    """
    """
    client = Client("192.168.99.100", 9000)
    for f in client.ls(['/files']):
        print f
        for line in client.cat([f.get('path')]):
            for l in line:
                print l

# ============================================================
if __name__ == '__main__':
    test()
