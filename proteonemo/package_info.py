# Copyright (c) 2021 Peptone.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License. 


MAJOR = 0
MINOR = 1
PATCH = 0
PRE_RELEASE = ''

# Use the following formatting: (major, minor, patch, pre-release)
VERSION = (MAJOR, MINOR, PATCH, PRE_RELEASE)

__shortversion__ = '.'.join(map(str, VERSION[:3]))
__version__ = '.'.join(map(str, VERSION[:3])) + ''.join(VERSION[3:])

__package_name__ = 'proteonemo'
__contact_names__ = 'Peptone'
__contact_emails__ = 'carlo@peptone.io'
__homepage__ = 'https://peptone.io/'
__repository_url__ = 'https://github.com/PeptoneInc/ProteoNeMo.git'
__download_url__ = 'https://github.com/PeptoneInc/ProteoNeMo/archive/refs/heads/main.zip'
__description__ = 'ProteoNeMo - protein embeddings at scale'
__license__ = 'Apache2'
__keywords__ = 'protein, embedding, deep learning, machine learning, gpu, NeMo, peptone, pytorch, torch, tts'