from __future__ import absolute_import
__author__ = 'katharine'

import pypkjs.PyV8 as v8
import time


class Performance(object):
    # This is an approximation for now
    def __init__(self, runtime):
        runtime.natives['time'] = time.time
        with runtime.context as ctx:
            ctx.eval("""
            performance = new (function() {
                var _time = _from_python('time');
                var start = _time();

                this.now = function() {
                    return (_time() - start) * 1000;
                };
            })();
            """)
