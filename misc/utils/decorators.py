import time
from functools import wraps


def dump_closure(f):
    if hasattr(f, "func_closure") and f.func_closure is not None:
        print "- Dumping function closure for %s:" % f.__name__
        for i, c in enumerate(f.func_closure):
            print "-- cell %d  = %s" % (i, c.cell_contents)
    else:
        print " - %s has no closure!" % f.__name__


def memoize(func):
    cache = {}
    @wraps(func)
    def memoized_f(*args, **kwargs):
        key = repr(args) + repr(kwargs)
        if key in cache:
            return cache[key]
        result = func(*args, **kwargs)
        cache[key] = result
        return result
    memoized_f._cache = cache
    return memoized_f


def cached(timeout, logged=False):
    """Decorator to cache the result of a function call.
    Cache expires after timeout seconds.
    """

    def decorator(func):
        if logged:
            print "-- Initializing cache for", func.__name__
        cache = {}

        @wraps(func)
        def decorated_function(*args, **kwargs):
            if logged:
                print "-- Called function", func.__name__
            key = repr(args) + repr(kwargs)
            result = None
            if key in cache:
                if logged:
                    print "-- Cache hit for", func.__name__, key

                (cache_hit, expiry) = cache[key]
                if time.time() - expiry < timeout:
                    result = cache_hit
                elif logged:
                    print "-- Cache expired for", func.__name__, key
            elif logged:
                print "-- Cache miss for", func.__name__, key

            # No cache hit, or expired
            if result is None:
                result = func(*args, **kwargs)
                cache[key] = (result, time.time())
            return result

        return decorated_function

    return decorator


def logged(time_format="%b %d %Y - %H:%M:%S", name_prefix=""):
    def decorator(func):
        if hasattr(func, '_logged_decorator') and func._logged_decorator:
            return func

        @wraps(func)
        def decorated_func(*args, **kwargs):
            start_time = time.time()
            print "- Running '%s' on %s " % (
                name_prefix + func.__name__,
                time.strftime(time_format)
            )
            result = func(*args, **kwargs)
            end_time = time.time()
            print "- Finished '%s', execution time = %0.3fs " % (
                name_prefix + func.__name__,
                end_time - start_time
            )

            return result
        decorated_func._logged_decorator = True
        return decorated_func
    return decorator


def log_method_calls(time_format):
    def decorator(cls):
        for o in dir(cls):
            if o.startswith('__'):
                continue
            a = getattr(cls, o)
            if hasattr(a, '__call__'):
                decorated_a = logged(time_format, cls.__name__ + ".")(a)
                setattr(cls, o, decorated_a)
        return cls
    return decorator
