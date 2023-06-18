from kink import di

from repository import Repository
from service_a import ServiceA
from service_b import ServiceB
from service_c import ServiceC

def bootstrap_dependencies():
    di[Repository] = Repository()
    di[ServiceC] = ServiceC(di[Repository])
    di[ServiceB] = ServiceB(di[Repository], di[ServiceC])
    di[ServiceA] = ServiceA(di[Repository], di[ServiceB])