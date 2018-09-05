
# coding: utf-8

# ### RE Generator
# 
# See: https://classroom.udacity.com/courses/cs212/lessons/48738183
# 
# This notebook want to test idean of genseq() function. Seems that it will cause infinite loop, but difficult to figure this problem out. So use this notebook to test this idea.

# In[42]:


import functools

def track(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kargs):
        print("{}({})".format(
            fn.__name__, 
            ", ".join(map(lambda arg: arg.__repr__(), args)), 
            ", ".join(["{}={}".format(name, val) for name, val in kargs.items()])))
        return fn(*args, **kargs)
    return wrapper


# In[47]:


@track
def lit(s):         
    return lambda Ns: set([s]) if len(s) in Ns else null

@track
def star(x):        
    return lambda Ns: opt(plus(x))(Ns)

@track
def opt(x):         
    return alt(epsilon, x)

@track
def alt(x, y):      
    return lambda Ns: set(x(Ns)) | set(y(Ns))

"""
@track
def plus(x):        
    return lambda Ns: genseq(x, star(x), Ns)
"""

epsilon = lit('') 
null = frozenset([])

"""
@track
def genseq(x, y, Ns):
    MNs = range(max(Ns) + 1)
    return set([m1 + m2 
               for m1 in x(MNs)
               for m2 in y(MNs)
               if len(m1+m2) in Ns])
"""

@track
def plus(x):        
    return lambda Ns: genseq(x, star(x), Ns, startx=1)

@track
def genseq(x, y, Ns, startx=0):
    if not Ns:
        return null
    xmatches = x(range(startx, max(Ns) + 1))
    Ns_x = set([len(m) for m in xmatches])
    Ns_y = set([n-m for n in Ns for m in Ns_x if n-m >= 0])
    ymatches = y(Ns_y)
    return set([m1 + m2 
               for m1 in xmatches
               for m2 in ymatches
               if len(m1+m2) in Ns])
        


# In[36]:


print(genseq(lit('a'), lit('b'), [2]))


# In[49]:


print(plus(opt(lit('a')))([2, 4]))


# In[50]:


print(plus(star(lit('a')))([2, 4]))

