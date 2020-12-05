# -*- coding: utf-8 -*-
#
# Copyright (c) 2020~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from typing import *
from abc import ABC, abstractmethod
from logging import Logger
from dataclasses import dataclass

import fsoopify

@dataclass
class Metadata:
    priority: int
    value: Any
    infer_from: str = ''
    metadata_id: str = None # auto generated


class IProject(ABC):
    'the project interface.'

    @property
    @abstractmethod
    def root_dir(self) -> fsoopify.DirectoryInfo:
        'the root dir (abs)path of the project.'
        raise NotImplementedError

    @abstractmethod
    def read_text(self, path: str, relative: bool=True, cached: bool=True) -> Optional[str]:
        '''
        try read text from `path`.

        return `None` if the file is not exists.
        '''
        raise NotImplementedError


class IMetadataResolveContext(ABC):
    'the context interface.'

    @property
    @abstractmethod
    def project(self) -> IProject:
        raise NotImplementedError

    @property
    @abstractmethod
    def logger(self) -> Logger:
        raise NotImplementedError

    @abstractmethod
    def set_result(self, name: str, result: Metadata):
        'set result with metadata name.'
        raise NotImplementedError


class IMetadataProvider(ABC):
    'the metadata provider interface.'

    @abstractmethod
    def get_provided(self) -> Union[List[str], str]:
        'get all provided metadata names, use for determine resolve order.'
        raise NotImplementedError

    def get_dependencies(self) -> Union[List[str], str]:
        'get all depended metadata names, use for determine resolve order.'
        return []

    @abstractmethod
    def run(self, context: IMetadataResolveContext, deps: Dict[str, List[Metadata]]):
        raise NotImplementedError


class ISorter(ABC):
    'the metadata provider interface.'

    attr_name: str = None

    @abstractmethod
    def sort(self, name: str, metadatas: List[Metadata]) -> List[Metadata]:
        'sort the metadatas.'
        raise NotImplementedError


class IAttrPicker(ABC):
    'the metadata provider interface.'

    attr_name: str = None

    @abstractmethod
    def write(self, name: str, metadatas: List[Metadata], attrs: Dict[str, Any]):
        'write metadata into attrs.'
        raise NotImplementedError


def exported(cls):
    'mark the class as a implemented class.'
    cls._smb_exported = True
    return cls
