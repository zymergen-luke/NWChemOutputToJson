##############################################################################
# This source file is part of the NWChemOutputToJson project.
# Copyright (c) 2016, The Regents of the University of California, through
# Lawrence Berkeley National Laboratory (subject to receipt of any required
# approvals from the U.S. Dept. of Energy).
# This source code is released under the BSD 3-Clause License, (the "License").
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
##############################################################################
from __future__ import absolute_import
import argparse

from nwchem2json import nwchemToJson


def main(argv=None):
  parser = argparse.ArgumentParser()
  parser.add_argument('files', nargs='*', help='files to parse')
  parser.add_argument(
    '--no-orbitals', action='store_false', default=True, dest='orbitals',
    help='Dont include orbitals in output')
  parser.add_argument(
    '-o', type=argparse.FileType('w'), dest='outfile',
    help='Output json file to write')
  args = parser.parse_args(argv)

  if len(args.files) > 1 and args.outfile:
    parser.error('may not specify -o when converting multiple files')

  for filename in args.files:
    with open(filename) as handle:
      jsonObj = nwchemToJson.nwchemToJson(processOrbitals=args.orbitals)
      converted_content = jsonObj.convert(handle)

      if args.outfile:
        args.outfile.write(converted_content)
      else:
        with open(filename + '.json', 'w') as outfile:
          outfile.write(converted_content)


if __name__ == '__main__':
    main()