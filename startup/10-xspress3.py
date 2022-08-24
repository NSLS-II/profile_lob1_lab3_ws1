from ophyd import Component

from nslsii.areadetector.xspress3 import (
    build_xspress3_class,
    Xspress3Detector,
    Xspress3HDF5Plugin,
    Xspress3Trigger
)


xs3_class = build_xspress3_class(
    channel_numbers=(1, 2, 3, 4),
    mcaroi_numbers=(1, 2, 3, 4),
    image_data_key="image",
    xspress3_parent_classes=(Xspress3Trigger, Xspress3Detector),
    extra_class_members={
        "hdf5plugin": Component(
            Xspress3HDF5Plugin,
            name="h5p",
            prefix="XF:05IDD-ES{Xsp:1}:HDF1:",
            root_path="/nsls2/data/staff/jlynch/",
            path_template="/nsls2/data/staff/jlynch/data",
            resource_kwargs={}
        )
    }
)

xs3 = xs3_class(prefix="XF:05IDD-ES{Xsp:1}:", name="xs3")


from bluesky import RunEngine
from bluesky.plans import count

from event_model import Filler
from area_detector_handlers.handlers import Xspress3HDF5Handler

from ophyd import Kind

xs3.hdf5plugin.kind = Kind.normal

xs3.hdf5plugin.read_attrs

xs3.channel01.image.kind = Kind.normal
xs3.channel01.kind = Kind.normal

document_list = []

def append_document(name, doc):
    document_list.append((name, doc))


RE = RunEngine()

RE.subscribe(append_document)

