__author__ = "soopercool101"
__version__ = "1.0.0"

from BrawlCrate.API import BrawlAPI
from System.IO import Path

BrawlAPI.OpenTemplate(Path.Combine(BrawlAPI.PluginPath, "Project M 3.6 Stage Templates", "STGVILLAGE.pac"))