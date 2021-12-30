
import argparse
# commandline
# file case collection

"""
{
    "name":"",
    headers:{};
    "apis":[
        {
            "api_name":"",
            "api_url":"",
            "api_method":"",
            "headers":{},
            "cases":[
                {
                    "queries":{},
                    "headers":{},
                    "body":{},
                    "expect":{},
                },
                {}
            ] 
        }
        {}
    ]
}
"""


# def __init__(self,
#              prog=None,
#              usage=None,
#              description=None,
#              epilog=None,
#              parents=[],
#              formatter_class=HelpFormatter,
#              prefix_chars='-',
#              fromfile_prefix_chars=None,
#              argument_default=None,
#              conflict_handler='error',
#              add_help=True,
#              allow_abbrev=True):

# - prog -- The name of the program (default: sys.argv[0])
# - usage -- A usage message (default: auto-generated from arguments)
# - description -- A description of what the program does
# - epilog -- Text following the argument descriptions
# - parents -- Parsers whose arguments should be copied into this one
# - formatter_class -- HelpFormatter class for printing help messages
# - prefix_chars -- Characters that prefix optional arguments
# - fromfile_prefix_chars -- Characters that prefix files containing
#     additional arguments
# - argument_default -- The default value for all arguments
# - conflict_handler -- String indicating how to handle conflicts
# - add_help -- Add a -h/-help option
# - allow_abbrev -- Allow long options to be abbreviated unambiguously
parser: argparse.ArgumentParser = argparse.ArgumentParser(
    prog="webtest", description="命令行快速测试或使用case集文件驱动测试")
exclusive = parser.add_mutually_exclusive_group()
exclusive.add_argument("--command")
exclusive.add_argument_group()
exclusive.add_argument("--file")
if __name__ == "__main__":
    args = parser.parse_args()
    # show --help
    # handle commandline
    # --command -url -method -body
    # handle case collection in file
    # --file    -f
    pass
