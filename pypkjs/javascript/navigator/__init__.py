__author__ = 'katharine'

import STPyV8 as v8
from .geolocation import Geolocation


class Navigator(object):
    def __init__(self, runtime):
        self._runtime = runtime
        runtime.natives['location'] = Geolocation(runtime)
        with runtime.context as ctx:
            ctx.eval("""
            navigator = new (function() {
                this.language = 'en-GB';
                var location = _from_python('location');
                if(true) { // TODO: this should be a check on geolocation being enabled.
                    this.geolocation = new (function() {
                        _make_proxies(this, location, ['getCurrentPosition', 'watchPosition', 'clearWatch']);
                    })();
                }
            })();
            """)
