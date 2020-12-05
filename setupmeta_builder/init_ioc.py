# -*- coding: utf-8 -*-
#
# Copyright (c) 2020~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

def conf_ioc(ioc):
    from .abc import ISorter, IAttrPicker, IMetadataProvider

    from .provs import _

    for cls in IMetadataProvider.__subclasses__():
        if getattr(cls, '_smb_exported', False):
            ioc.register_scoped('MetadataProvider', cls)

    from .sorters import DefaultSorter

    ioc.register_scoped('Sorter', DefaultSorter)
    for cls in ISorter.__subclasses__():
        if cls.attr_name is not None:
            ioc.register_scoped(f'Sorter[{cls.attr_name}]', cls)

    from .pickers import DefaultAttrPicker

    ioc.register_scoped('AttrPicker', DefaultAttrPicker)
    for cls in IAttrPicker.__subclasses__():
        if cls.attr_name is not None:
            ioc.register_scoped(f'AttrPicker[{cls.attr_name}]', cls)
