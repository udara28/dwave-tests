from dimod.reference.samplers import ExactSolver
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
import dwave_networkx as dnx
import networkx as nx

s5 = nx.star_graph(4)

sampler = ExactSolver()
result = dnx.min_vertex_cover(s5, sampler)

print('Result from local solver :')
print(result)
print('\n')

sampler = EmbeddingComposite(DWaveSampler(solver='DW_2000Q_2_1'))
result = dnx.min_vertex_cover(s5, sampler)


print('Result from leap solver :')
print(result)
print('\n')
