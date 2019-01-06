from dwave.cloud import Client
from dwave.system.samplers import DWaveSampler
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
import dimod
import neal

#client = Client.from_config(token='')
#client.get_solvers()

#sampler = DWaveSampler()
#sampler.parameters


# Using ExactSolver (Local solver)
print('Using ExactSolver...')

solver = dimod.ExactSolver()
response = solver.sample_ising({'a': -0.5, 'b': 1.0}, {('a', 'b'): -1})
result = response.data_vectors['energy']
print(result)


# Using neal (Local solver)
print('Using SimulatedAnnealingSampler...')

solver = neal.SimulatedAnnealingSampler()
response = solver.sample_ising({'a': -0.5, 'b': 1.0}, {('a', 'b'): -1})
result = response.data_vectors['energy']
print(result)


# Using D-Wave sampler
print('Using D-Wave solver')


solver = EmbeddingComposite(DWaveSampler(solver='DW_2000Q_2_1'))
response = solver.sample_ising({'a': -0.5, 'b': 1.0}, {('a', 'b'): -1})
result = response.data_vectors['energy']
print(result)
