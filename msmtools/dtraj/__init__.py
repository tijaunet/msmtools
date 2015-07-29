
# Copyright (c) 2015, 2014 Computational Molecular Biology Group, Free University
# Berlin, 14195 Berlin, Germany.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
#  * Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation and/or
# other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS ``AS IS''
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

r"""

===============================================================
dtraj - Discrete trajectories functions (:mod:`msmtools.dtraj`)
===============================================================

.. currentmodule:: msmtools.dtraj

Discrete trajectory io
======================

.. autosummary::
   :toctree: generated/

   read_discrete_trajectory - read microstate trajectoryfrom ascii file
   read_dtraj
   write_discrete_trajectory - write microstate trajectory to ascii file
   write_dtraj
   load_discrete_trajectory - read microstate trajectoryfrom biqqnary file
   load_dtraj
   save_discrete_trajectory -  write microstate trajectory to binary file
   save_dtraj

Simple statistics
=================

.. autosummary::
   :toctree: generated/

   count_states
   visited_set
   number_of_states
   index_states

Sampling trajectory indexes
===========================

.. autosummary::
   :toctree: generated/

   sample_indexes_by_distribution
   sample_indexes_by_state
   sample_indexes_by_sequence

"""
from __future__ import absolute_import
from .api import *
