# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.camino.odf import SFPeaks
def test_SFPeaks_inputs():
    input_map = dict(ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    stdsfrommean=dict(units='NA',
    argstr='-stdsfrommean %f',
    ),
    mepointset=dict(units='NA',
    argstr='-mepointset %d',
    ),
    rbfpointset=dict(units='NA',
    argstr='-rbfpointset %d',
    ),
    out_file=dict(position=-1,
    genfile=True,
    argstr='> %s',
    ),
    density=dict(units='NA',
    argstr='-density %d',
    ),
    scheme_file=dict(argstr='%s',
    ),
    args=dict(argstr='%s',
    ),
    pdthresh=dict(units='NA',
    argstr='-pdthresh %f',
    ),
    inputmodel=dict(mandatory=True,
    argstr='-inputmodel %s',
    ),
    pointset=dict(units='NA',
    argstr='-pointset %d',
    ),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(mandatory=True,
    argstr='-inputfile %s',
    ),
    numpds=dict(units='NA',
    argstr='-numpds %d',
    ),
    searchradius=dict(units='NA',
    argstr='-searchradius %f',
    ),
    noconsistencycheck=dict(argstr='-noconsistencycheck',
    ),
    order=dict(units='NA',
    argstr='-order %d',
    ),
    )
    inputs = SFPeaks.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value
def test_SFPeaks_outputs():
    output_map = dict(peaks=dict(),
    )
    outputs = SFPeaks.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value