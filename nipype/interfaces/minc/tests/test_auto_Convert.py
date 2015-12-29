# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ....testing import assert_equal
from ..minc2 import Convert


def test_Convert_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    chunk=dict(argstr='-chunk %d',
    usedefault=False,
    ),
    clobber=dict(argstr='-clobber',
    usedefault=True,
    ),
    compression=dict(argstr='-compress %s',
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
    output_file=dict(argstr='%s',
    genfile=True,
    hash_files=False,
    name_source=['input_file'],
    name_template='%s_convert_output.mnc',
    position=-1,
    ),
    template=dict(argstr='-template',
    ),
    terminal_output=dict(nohash=True,
    ),
    two=dict(argstr='-2',
    ),
    )
    inputs = Convert.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value


def test_Convert_outputs():
    output_map = dict(output_file=dict(),
    )
    outputs = Convert.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
