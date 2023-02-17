#!/usr/bin/env python
# coding: utf-8

# In[1]:


from win10toast import ToastNotifier


# In[3]:


notifier=ToastNotifier()


# In[8]:


new_cases="127"


# In[9]:


message="New case"+new_cases+"\nDeath 125"


# In[10]:


message


# In[12]:


notifier.show_toast(title="Covid-19 update",msg=message,duration=5) # you can specify the icon icon_path="icon.icon"


# In[ ]:




