def dump_closure(f):
   if hasattr(f, "__closure__") and f.__closure__ is not None:
       print "- Dumping function closure for %s:" % f.__name__
       for i, c in enumerate(f.__closure__):
           print "-- cell %d  = %s" % (i, c.cell_contents)
   else:
       print " - %s has no closure!" % f.__name__
