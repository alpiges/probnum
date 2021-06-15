"""Quadrature / Numerical Integration of Functions.

This package implements Bayesian quadrature rules used for numerical
integration of functions on a given domain. Such methods integrate a
function by iteratively building a probabilistic model and adaptively
choosing points to evaluate the integrand based on said model.
"""

from ._bayesquad import bayesquad, bayesquad_fixed
from ._integration_measures import GaussianMeasure, IntegrationMeasure, LebesgueMeasure
from .acquisitions import Acquisition
from .bq_methods import (
    BayesianQuadrature,
    BQBeliefUpdate,
    BQInfo,
    BQStandardBeliefUpdate,
    BQState,
)
from .kernel_embeddings import (
    KernelEmbedding,
    _kernel_mean_expquad_gauss,
    _kernel_mean_expquad_lebesgue,
    _kernel_variance_expquad_gauss,
    _kernel_variance_expquad_lebesgue,
)
from .policies import OptimalPolicy, Policy, RandomPolicy
from .stop_criteria import (
    IntegralVarianceTolerance,
    MaxNevals,
    RelativeMeanChange,
    StoppingCriterion,
)

# Public classes and functions. Order is reflected in documentation.
__all__ = [
    "bayesquad",
    "bayesquad_fixed",
    "BayesianQuadrature",
    "IntegrationMeasure",
    "KernelEmbedding",
    "GaussianMeasure",
    "LebesgueMeasure",
    "StoppingCriterion",
]

# Set correct module paths. Corrects links and module paths in documentation.
BayesianQuadrature.__module__ = "probnum.quad"
IntegrationMeasure.__module__ = "probnum.quad"
KernelEmbedding.__module__ = "probnum.quad"
GaussianMeasure.__module__ = "probnum.quad"
LebesgueMeasure.__module__ = "probnum.quad"
StoppingCriterion.__module__ = "probnum.quad"
