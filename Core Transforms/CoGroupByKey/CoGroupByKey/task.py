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

from log_elements import LogElements


class WordsAlphabet:

    def __init__(self, alphabet, fruit, country):
        self.alphabet = alphabet
        self.fruit = fruit
        self.country = country

    def __str__(self):
        return "WordsAlphabet(alphabet:'%s', fruit='%s', country='%s')" % (self.alphabet, self.fruit, self.country)


def apply_transforms(fruits, countries):
    fruit_kv = fruits | beam.Map(lambda x: (x[0], x))
    countries_kv = countries | beam.Map(lambda x: (x[0], x))
    joined_data = (
            {"fruit": fruit_kv, "country": countries_kv}
            | beam.CoGroupByKey()
            | beam.Map(lambda x: str(WordsAlphabet(x[0], x[1]["fruit"][0], x[1]["country"][0])))
    )
    return joined_data


with beam.Pipeline() as p:
    fruits = p | 'Fruits' >> beam.Create(['apple', 'banana', 'cherry'])
    countries = p | 'Countries' >> beam.Create(['australia', 'brazil', 'canada'])

    results = (apply_transforms(fruits, countries)
               | LogElements())
