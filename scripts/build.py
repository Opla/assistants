# Copyright 2024 mik
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from datetime import UTC, datetime
import json
import os
from jsonschema import validate
import json


collection = {
    "_version": "1",
    "created_at": datetime.now(tz=UTC).strftime("%Y-%m-%dT%H:%M:%S%.%fZ"),
    "updated_at": datetime.now(tz=UTC).strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
    "assistants": [],
    "tags": [],
}

def add_assistant(assistant):
    collection['assistants'].append(assistant)

def add_assistants(path):
    if os.path.isdir(path):
        for file in os.listdir(path):
            add_assistants(os.path.join(path, file))
    else:
        with open(path, 'r') as f:
            assistant = json.load(f)
            add_assistant(assistant)

def build():
    add_assistants('./assistants')
    with open('./schema/v1/assistants_collection.schema.json', 'r') as f:
        schema = json.load(f)

        validate(collection, schema)

if __name__ == "__main__":
    build()
    with open("all.json", 'w') as f:
        json.dump(collection, f)