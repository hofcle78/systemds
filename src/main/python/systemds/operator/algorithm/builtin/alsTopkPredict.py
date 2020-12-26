# -------------------------------------------------------------
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
# -------------------------------------------------------------

from typing import Dict

from systemds.operator import OperationNode
from systemds.script_building.dag import OutputType
from systemds.utils.consts import VALID_INPUT_TYPES
 
def alsTopkPredict(userIDs: OperationNode, I: OperationNode, L: OperationNode, R: OperationNode, **kwargs: Dict[str, VALID_INPUT_TYPES]) -> OperationNode:
    """
    :param userIDs: Column vector of user-ids (n x 1)
    :param I: Indicator matrix user-id x user-id to exclude from scoring
    :param L: The factor matrix L: user-id x feature-id
    :param R: The factor matrix R: feature-id x item-id
    :param K: The number of top-K items
    :return: 'OperationNode' containing users (rows) & a matrix containing the top-k predicted ratings for the specified users (rows) 
    """
    
    userIDs._check_matrix_op()
    if userIDs.shape[0] == 0:
        raise ValueError("Found array with 0 feature(s) (shape={s}) while a minimum of 1 is required."
                         .format(s=userIDs.shape))
    I._check_matrix_op()
    if I.shape[0] == 0:
        raise ValueError("Found array with 0 feature(s) (shape={s}) while a minimum of 1 is required."
                         .format(s=I.shape))
    L._check_matrix_op()
    if L.shape[0] == 0:
        raise ValueError("Found array with 0 feature(s) (shape={s}) while a minimum of 1 is required."
                         .format(s=L.shape))
    R._check_matrix_op()
    if R.shape[0] == 0:
        raise ValueError("Found array with 0 feature(s) (shape={s}) while a minimum of 1 is required."
                         .format(s=R.shape))
    params_dict = {'userIDs':userIDs, 'I':I, 'L':L, 'R':R}
    params_dict.update(kwargs)
    return OperationNode(userIDs.sds_context, 'alsTopkPredict', named_input_nodes=params_dict, output_type=OutputType.LIST, number_of_outputs=2, output_types=[OutputType.MATRIX, OutputType.MATRIX])


    