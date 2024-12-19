class TooManyRequestError(Exception):
    def __str__(self):
            return "Request melebih kapasitas,silahkan coba beberapa saat lagi"


class Throttler(object):
    cache = {}

    # sintaks def __init__ untuk melakukan inisiasi beberapa
    # parameter yang dibutuhkan
    def __init__(self,max_rate,window,throttle_stop=False,cache_age=1800):
        self.max_rate = max_rate

        self.window = window

        self.throttle_stop = throttle_stop

        self.cache_age = cache_age

        self.next_reset_at = dict()
        self.num_request = dict()

        now = datetime.datetime.now()
        for source in self.max_rate:
            self.next_reset_at[source] = now + datetime.timedelta(seconds=self.window.get(source))
            self.num_requests[source] = 0
    
    def request(self, source, method, do_cache=False):
        now = datetime.datetime.now()

        
        key = source + method.func_name
        if do_cache and key in self.cache:
            timestamp, data = self.cache.get(key)
            logging.info('{} exists in cached @ {}'.format(key, timestamp))

            if (now - timestamp).seconds < self.cache_age:
                logging.info('retrieved cache for {}'.format(key))
                return data

       

        
        if now > self.next_reset_at.get(source):
            self.num_requests[source] = 0
            self.next_reset_at[source] = now + datetime.timedelta(seconds=self.window.get(source))

        
        def halt(wait_time):
            if self.throttle_stop:
                raise TooManyRequestsError()
            else:
                
                time.sleep(wait_time + 0.1)

        # untuk validasi apakah request melebih dari jumlah request yang sudah ditentukan?
        if self.num_requests.get(source) >= self.max_rate.get(source):
            logging.info('back off: {} until {}'.format(source, self.next_reset_at.get(source)))
            halt((self.next_reset_at.get(source) - now).seconds)

        self.num_requests[source] += 1
        response = method()  # potential exception raise

        
        if do_cache:
            self.cache[key] = (now, response)
            logging.info('cached instance for {}, {}'.format(source, method))

        return response

# Contoh penggunaan
max_rate = {'source_1': 50}  # maksimal 50 request
window = {'source_1': 60}    # waktu yang ditetapkan
throttler = Throttler(max_rate=max_rate, window=window)