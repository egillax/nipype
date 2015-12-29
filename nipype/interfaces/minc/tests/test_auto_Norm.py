# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ....testing import assert_equal
from ..minc2 import Norm


def test_Norm_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    clamp=dict(argstr='-clamp',
    usedefault=True,
    ),
    clobber=dict(argstr='-clobber',
    usedefault=True,
    ),
    cutoff=dict(argstr='-cutoff %s',
    max=100,
    min=0,
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
    lower=dict(argstr='-lower %s',
    ),
    mask=dict(argstr='-mask %s',
    ),
    out_ceil=dict(argstr='-out_ceil %s',
    ),
    out_floor=dict(argstr='-out_floor %s',
    ),
    output_file=dict(argstr='%s',
    genfile=True,
    hash_files=False,
    name_source=['input_file'],
    name_template='%s_norm.mnc',
    position=-1,
    ),
    output_threshold_mask=dict(argstr='-threshold_mask %s',
    hash_files=False,
    name_source=['input_file'],
    name_template='%s_norm_threshold_mask.mnc',
    ),
    terminal_output=dict(nohash=True,
    ),
    threshold=dict(argstr='-threshold',
    ),
    threshold_blur=dict(argstr='-threshold_blur %s',
    ),
    threshold_bmt=dict(argstr='-threshold_bmt',
    ),
    threshold_perc=dict(argstr='-threshold_perc %s',
    max=100,
    min=0,
    ),
    upper=dict(argstr='-upper %s',
    ),
    )
    inputs = Norm.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value


def test_Norm_outputs():
    output_map = dict(output_file=dict(),
    output_threshold_mask=dict(),
    )
    outputs = Norm.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
