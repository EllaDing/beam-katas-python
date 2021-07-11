#   Licensed to the Apache Software Foundation (ASF) under one
#   or more contributor license agreements.  See the NOTICE file
#   distributed with this work for additional information
#   regarding copyright ownership.  The ASF licenses this file
#   to you under the Apache License, Version 2.0 (the
#   "License"); you may not use this file except in compliance
#   with the License.  You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import apache_beam as beam

# Each step in the pipeline is delimited by the pipe operator `|`.
# The outputs of each transform are passed to the next transform as inputs.
# And we can save the final results into a `PCollection` variable.
with beam.Pipeline() as p:
    outputs = (p
               | "create data" >> beam.transforms.core.Create(["Hello Beam"]))
    # `outputs` is a PCollection with our input elements.
    # But printing it directly won't show us its contents :(
    outputs | beam.Map(print)
