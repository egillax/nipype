# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ....testing import assert_equal
from ..minc2 import Voliso


def test_Voliso_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    avgstep=dict(argstr='--avgstep',
    ),
    clobber=dict(argstr='--clobber',
    usedefault=True,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    input_file=dict(argstr='%s',
    mandatory=True,
    position=-2,
    ),
    maxstep=dict(argstr='--maxstep %s',
    ),
    minstep=dict(argstr='--minstep %s',
    ),
    output_file=dict(argstr='%s',
    genfile=True,
    hash_files=False,
    name_source=['input_file'],
    name_template='%s_voliso.mnc',
    position=-1,
    ),
    terminal_output=dict(nohash=True,
    ),
    verbose=dict(argstr='--verbose',
    ),
    )
    inputs = Voliso.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value


def test_Voliso_outputs():
    output_map = dict(output_file=dict(),
    )
    outputs = Voliso.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
