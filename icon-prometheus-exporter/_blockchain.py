# Copyright (C) 2019  MixBytes, LLC
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND (express or implied).
from icon_prometheus_exporter._rpc import get_block_num

class BlockCache:
    """
    Simple code which caches blocks.
    """

    def __init__(self, rpc, size=256):
        self._rpc = rpc
        self.size = size
        # hash
        self._cache = dict()

    # def get(self, peer_id):
    #     peer_id = peer_id.lower()
    #
    #     # if peer_id not in self._cache:
    #     #     # block = self._rpc.request('chain_getBlock', [peer_id])['result']
    #     #     # print("blackness's {%s}".format(block))
    #     #     if block is None:
    #     #         # not caching negative results
    #     #         return None
    #
    #         # the simplest cleanup algorithm with amortized constant time complexity
    #         # if len(self._cache) >= self.size * 2:
    #         #     ordered_by_block_num = sorted(self._cache.items(), key=lambda i: get_block_num(i[1]), reverse=True)
    #         #     self._cache = dict(ordered_by_block_num[:self.size])
    #         self._cache[peer_id] = block
    #     return self._cache[peer_id]
