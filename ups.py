#!/usr/bin/env python
# coding: utf-8

# In[135]:


from plumbum.cmd import apcaccess
from datadog_checks.checks import AgentCheck


# In[136]:


class ups(AgentCheck):
    def check(self, instance):
        timeleft=apcaccess["-p","TIMELEFT"]()
        timeleft=str(timeleft)
        timeleft=timeleft.split()
        self.gauge('ups.timeleft',timeleft[0])
        
        charge=apcaccess["-p","BCHARGE"]()
        charge=str(charge)
        charge=charge.split(" ")
        charge[0]
        self.gauge('ups.charge',charge[0])

        status=apcaccess["-p","STATUS"]()
        status=str(status)
        if status=="ONLINE \n":
            self.gauge('ups.status',1)
        else:
            self.gauge('ups.status',0)
        
    


# In[ ]:




