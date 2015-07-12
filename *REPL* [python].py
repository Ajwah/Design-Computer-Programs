Warning: No active frommets remain. Continue?
((8, 10), <itertools._grouper object at 0x107fc5ed0>)
((8, 9), <itertools._grouper object at 0x107fc5f10>)
((0, [11, 9, 8, 7, 6]), <itertools._grouper object at 0x10804ab10>)
((5, [10, 8, 7, 6, 5]), <itertools._grouper object at 0x10804ab90>)
((0, [11, 10, 8, 7, 6]), <itertools._grouper object at 0x10804abd0>)
((0, [11, 8, 7, 6, 5]), <itertools._grouper object at 0x10804ac10>)
((5, [10, 9, 7, 6, 5]), <itertools._grouper object at 0x10804ac50>)
((0, [11, 10, 9, 7, 6]), <itertools._grouper object at 0x10804ac90>)
((0, [11, 9, 7, 6, 5]), <itertools._grouper object at 0x10804acd0>)
((0, [11, 10, 7, 6, 5]), <itertools._grouper object at 0x10804ad10>)
((5, [10, 9, 8, 6, 5]), <itertools._grouper object at 0x10804ad50>)
((0, [11, 10, 9, 8, 6]), <itertools._grouper object at 0x10804ad90>)
((0, [11, 9, 8, 6, 5]), <itertools._grouper object at 0x10804add0>)
((0, [11, 10, 8, 6, 5]), <itertools._grouper object at 0x10804ae10>)
((0, [11, 10, 9, 6, 5]), <itertools._grouper object at 0x10804ae50>)
((5, [10, 9, 8, 7, 5]), <itertools._grouper object at 0x10804ae90>)
((4, 11), <itertools._grouper object at 0x10804aed0>)
((0, [11, 9, 8, 7, 5]), <itertools._grouper object at 0x10804af10>)
((0, [11, 10, 8, 7, 5]), <itertools._grouper object at 0x10804af50>)
((0, [11, 10, 9, 7, 5]), <itertools._grouper object at 0x10804af90>)
((0, [11, 10, 9, 8, 5]), <itertools._grouper object at 0x10804afd0>)
Traceback (most recent call last):
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/runpy.py", line 151, in _run_module_as_main
    mod_name, loader, code, fname = _get_module_details(mod_name)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/runpy.py", line 101, in _get_module_details
    loader = get_loader(mod_name)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/pkgutil.py", line 464, in get_loader
    return find_loader(fullname)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/pkgutil.py", line 474, in find_loader
    for importer in iter_importers(fullname):
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/pkgutil.py", line 430, in iter_importers
    __import__(pkg)
  File "testing.py", line 34, in <module>
    print test_best_hand()
  File "testing.py", line 25, in test_best_hand
    == ['6C', '7C', '8C', '9C', 'TC'])
AssertionError
>>>